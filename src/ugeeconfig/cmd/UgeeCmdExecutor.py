from ..DefaultConfigs import *
from ..xml.UgeeElement import *

from .UgeeCmdExceptions import *
from .UgeeCmdParser import *
from .Prop import *

from ..utils.utils import printf, str_startswith_insensitive, str_equals_insensitive



PARPAR_DRV = "drv"
PARPAR_KEYS = "keys"
PARPAR_MOUSE = "mouse"
PARPAR_FUNCT = "funct"
PARPAR_SYSOP = "sysop"
PARPAR_MULTIMEDIA = "multimedia"
PARPAR_ALL = "all"



class UgeeCmdExecutor(object):
    def __init__(self, operation):
        self.operation = operation


    def execute(self):
        ugeeInst = self.__handleFrom()
        Prop.setUgeeInst(ugeeInst)

        if self.operation.set > 0:
            self.__handleSet()
            self.__handleTo()

        elif self.operation.get > 0:
            self.__handleGet()

        elif self.operation.doc > 0:
            self.__handleDoc()

        elif self.operation.actids > 0:
            self.__handleActids()

        elif self.operation.xkeysyms > 0:
            self.__handleXKeysyms()



    def __handleFrom(self):
        if self.operation.fromP.count > 0:
            ugeeEl = UgeeElement()
            contents = XMLElement.readXML(self.operation.fromP.value)
            ugeeInst = ugeeEl.readFromElement(contents)

        elif self.operation.fromP.count == 0:
            ugeeInst = generate_default_config()

        return ugeeInst




    def __handleTo(self):
        ugeeEl = UgeeElement()
        root = ugeeEl.writeToElement(Object({"ugee": Prop.UGEE_INST, "pentbversion": PENTABLET_LISTS_VERSION}))

        if self.operation.toP.count > 0:
            XMLElement.writeXML(root, self.operation.toP.value)

        elif self.operation.toP.count == 0:
            printf(XMLElement.asXML(root).decode("utf-8"))




    def __handleSet(self):
        leaves, values, nExErrors, grpErrors = self.__siftPropsForSet()
        nLeaves = len(leaves)

        exceptLines = []
        for i in nExErrors:
            p, nonExistent = i
            propName = "%s.%s" % (p.getPropPath(), ".".join(nonExistent),)
            exceptLines.append("%s: Non-existent prop!" % (propName,))

        if len(exceptLines) > 0:
            raise UgeeCmdExecutorNonExistentPropException("\n".join(exceptLines))

        for p in grpErrors:
            exceptLines.append("%s: Non-existent prop!" % (p.getPropPath(),))

        if len(exceptLines) > 0:
            raise UgeeCmdExecutorNotALeafPropException("\n".join(exceptLines))


        # Process single leaf props, if we're here, it means no error was found
        for i in range(0, nLeaves):
            currP = leaves[i]
            currV = values[i]

            setter = currP.getSetter()
            params = currP.getParams()
            formatter = currP.getFormatter()
            if setter is None:
                raise UgeeCmdExecutorException("%s: NO SETTER" % (currP.getPropPath(),))

            else:
                pType = currP.getValueType()
                v = None
                try:
                    v = Value(currV)
                except ActionException as ex:
                    raise UgeeCmdExecutorException(ex)
                vType = v.getType()

                compatibleType = True
                if pType == PTYPE_DEFAULT_ACTION:
                    compatibleType = (vType == PTYPE_INTEGER or vType == PTYPE_STRING)
                elif pType == PTYPE_WHEEL_USAGE:
                    compatibleType = (vType == PTYPE_STRING)
                else:
                    compatibleType = (vType == pType)

                if not compatibleType:
                    raise UgeeCmdExecutorIncompatibleValueTypeException("%s: \"%s\" is an incompatible type for value, \"%s\" type expected" % (currP, currV, pType,))

                path = currP.getPropPath()

                setter(params, v)
                self.__printf(formatter(path, currV, True))




    def __handleGet(self):
        operands = []

        n = len(self.operation.props)
        if n == 0:
            rootP = Prop.HIERARCHY
            operands = list(rootP.getAvailableLeaves())

        else:
            leaves, groups, errors = self.__siftPropsGetDoc()

            # Gather all the lists into one
            operands = list(leaves)
            for i in groups:
                operands.extend(list(i.getAvailableLeaves()))
            operands.extend(list(errors))


        for p in operands:
            if isinstance(p, tuple):
                p, nonExistents = p
                if len(nonExistents) > 0:
                    self.__printf("%s.%s: Non-existent prop!" % (p.getPropPath(), ".".join(nonExistents)))
                    continue

            path = p.getPropPath()
            getter = p.getGetter()
            params = p.getParams()
            formatter = p.getFormatter()

            if getter is None:
                raise UgeeCmdExecutorException("%s: NO GETTER, somebody, help!" % (path,))

            else:
                vG = getter(params)
                self.__printf(formatter(path, vG, False))




    def __handleDoc(self):
        n = len(self.operation.props)
        if n == 0:
            rootP = Prop.HIERARCHY
            operands = list(rootP.getChildren())
        else:
            leaves, groups, errors = self.__siftPropsGetDoc(False)

            # Gather all the lists into one
            operands = list(leaves)
            for i in groups:
                if i not in operands:
                    operands.append(i)
                operands.extend(i.getChildren())
            operands.extend(list(errors))


        #print(list(map(lambda x : x.getPropPath(), operands)))

        for p in operands:
            if isinstance(p, tuple):
                p, nonExistents = p
                if len(nonExistents) > 0:
                    self.__printf("%s.%s: Non-existent prop!" % (p.getPropPath(), ".".join(nonExistents)))
                    continue

            path = p.getPropPath()
            description = p.getDescription()
            valueType = p.getValueType()
            if valueType is None:
                self.__printf("%s: %s" % (path, description,))
            else:
                self.__printf("%s: %s [%s]" % (path, description, valueType.upper()))




    def __siftPropsForSet(self):
        leaves = []
        values = []
        # These must be always reported as errors
        nExErrors = []
        grpErrors = []

        nProps = len(self.operation.props)

        # Remove double props, get the latest value used
        for i in range(0, nProps):
            currProp = self.operation.props[i]
            currVal = self.operation.values[i]
            p, nonExistents = Prop.searchPropByPath(currProp)

            if len(nonExistents) > 0 and (p, nonExistents,) not in nExErrors:
                nExErrors.append((p, nonExistents,))

            elif p.isLeaf():
                if p in leaves:
                    idx = leaves.index(p)
                    values[idx] = currVal
                else:
                    leaves.append(p)
                    values.append(currVal)

            elif p not in grpErrors:
                grpErrors.append(p)

        return (leaves, values, nExErrors, grpErrors,)




    def __siftPropsGetDoc(self, isGet=True):
        leaves = [] # Leaf prop
        groups = [] # Group prop
        leafErr = [] # Leaf prop with error, tThese must be always reported as errors
        groupErr = [] # Group prop with error


        # First, remove doubles and differentiate between the different types of props
        for i in self.operation.props:
            p, nonExistents = Prop.searchPropByPath(i)

            if len(nonExistents) > 0:
                if p.isLeaf() and (p, nonExistents,) not in leafErr:
                    leafErr.append((p, nonExistents,))

                elif (p, nonExistents,) not in groupErr:
                    groupErr.append((p, nonExistents,))

            elif p.isLeaf() and p not in leaves:
                leaves.append(p)

            elif p not in groups:
                groups.append(p)


        # Consider the groups with errors, test them as filters first, if anything is found, then get the derived props, otherwise, keep as errors
        pLeaf, pGroup, errrr = UgeeCmdExecutor.__getPropsByErrorFilter(groupErr, isGet)

        # Add errors
        errors = list(leafErr)
        errors.extend(errrr)

        # Filter doubles and derived from pGroup
        pGroup = UgeeCmdExecutor.__pruneProps(pGroup, groups, isGet)

        # Add to groups
        groups.extend(pGroup)

        # Filter doubles and derived from pLeaf
        pLeaf = UgeeCmdExecutor.__pruneProps(pLeaf, leaves, isGet)
        pLeaf = UgeeCmdExecutor.__pruneProps(pLeaf, groups, isGet)

        # Add to leaves
        leaves.extend(pLeaf)

        # Filter doubles and derived in leaves in respect to groups
        leaves = UgeeCmdExecutor.__pruneProps(leaves, groups, isGet)

        return (leaves, groups, errors,)



    # Remove leaves that can be derived from the available groups
    # according to the rule (isGet=True -> isDescedeantdOf, isGet=False -> isChildOf)
    # It returns a pruned list with all unneded props removed
    @staticmethod
    def __pruneProps(propls1, propls2, isGet):
        p1copy = list(propls1)
        p1Sz = len(p1copy)

        i = 0
        while i < p1Sz:
            currp = p1copy[i]

            for j in propls2:
                if currp == j or (isGet and currp.isDescendeantOf(j)) or\
                    (not isGet and currp.isChildOf(j)):
                    # If the rule DOES apply, remove the current prop, as it is not needed
                    del p1copy[i]
                    p1Sz -= 1
                    i -= 1

            i += 1

        return p1copy



    # Consider the groups with errors, test them as filters first, if anything is found, then get the derived props, otherwise, keep as errors
    @staticmethod
    def __getPropsByErrorFilter(groupErr, isGet):
        pLeaf = []
        pGroup = []

        errr = []
        for i in groupErr:
            p, nonExistent = i

            nonExistentProp = ""
            if not p.isRoot():
                nonExistentProp = "%s." % (p.getPropPath(),)
            nonExistentProp += ".".join(nonExistent)

            avLvs = p.searchDescendeantsByPropPath(nonExistentProp)

            if len(avLvs) == 0: # The non-existent prop didn't create anything, it's an actual error
                errr.append(i)
                continue

            # Separate groups from leaves, for easy elaboration
            for j in avLvs:
                if isGet and j.isLeaf() and j not in pLeaf:
                    # In "get",  we only need leaves
                    pLeaf.append(j)

                elif not isGet and j.isChildOf(p):
                    # In "doc", we need the exact children of a node
                    if j.isLeaf() and j not in pLeaf:
                        pLeaf.append(j)

                    elif j not in pGroup:
                        pGroup.append(j)

        return (pLeaf, pGroup, errr,)




    def __printf(self, message):
        printf(message + "\n", self.operation.toP.count == 0)




    def __handleActids(self):
        operands = []

        n = len(self.operation.props)
        if n == 0:
            self.operation.props = [PARPAR_ALL,]

        actids = getAvailableActIds()
        actSz = len(actids[0])
        values = self.__detectActidsFromParameters(actids)

        for i in values:
            idx = actids[1].index(i)
            actid = actids[0][idx]
            operands.append("%s (%d)" % (actid, i,))


        print("Here follows the actids:")
        print()
        for i in operands:
            print(i)



    def __detectActidsFromParameters(self, actids):
        allWasFound = False
        includedValues = []
        values = []

        currPar = None
        currActidGrp = None


        for i in self.operation.props:
            if str_equals_insensitive(i, PARPAR_ALL):
                currPar = PARPAR_ALL

            elif str_equals_insensitive(i, PARPAR_DRV):
                currPar = ACTID_DRV_TYPE
                currActidGrp = [ACTID_DRV_NOP,]

            elif str_equals_insensitive(i, PARPAR_KEYS):
                currPar = ACTID_KEYSTRK_TYPE
                currActidGrp = ACTID_KEYSTRK_VALUES

            elif str_equals_insensitive(i, PARPAR_MOUSE):
                currPar = ACTID_MOUSEK_TYPE
                currActidGrp = ACTID_MOUSEK_TYPE

            elif str_equals_insensitive(i, PARPAR_FUNCT):
                currPar = ACTID_FUNCT_TYPE
                currActidGrp = ACTID_FUNCT_VALUES

            elif str_equals_insensitive(i, PARPAR_SYSOP):
                currPar = ACTID_SYSOP_TYPE
                currActidGrp = ACTID_SYSOP_VALUES

            elif str_equals_insensitive(i, PARPAR_MULTIMEDIA):
                currPar = ACTID_MULTIM_TYPE
                currActidGrp = ACTID_MULTIM_VALUES

            else:
                raise UgeeCmdExecutorException("Error: operand \"%s\" is not valid for operator \"actids\"" % (i,))


            if not allWasFound:
                if currPar == PARPAR_ALL:
                    values = list(actids[1])
                    allWasFound = True

                elif currPar not in includedValues:
                    includedValues.append(currPar)
                    values.extend(currActidGrp)

        return values




    def __handleXKeysyms(self):
        print("Here follows the available X Keysyms:")
        print()
        for i in Xlib.XK.get_available_augmented_keynames():
            print(i)