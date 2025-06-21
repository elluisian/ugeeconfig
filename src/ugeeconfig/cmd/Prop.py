from copy import deepcopy

from ..utils.utils import str_equals_insensitive, str_startswith_insensitive, printf
from ..utils.Object import *
from ..utils.Stack import *
from ..utils.Node import *

from .Value import *
from .UgeeCmdExceptions import *



DEVICE_PROP_NAME = "DEVICE"
DESKKEYS_PROP_NAME = "deskkeys"



PROPT_ROOT = 0
PROPT_SINGLE_GROUP = 1
PROPT_SINGLE_AS_MULTI_RESULT = 2
PROPT_MULTI_GROUP = 3
PROPT_LEAF = 4



DEBUG_GENERATION = False



class Prop(Node):
    HIERARCHY_GRAMMAR = None
    HIERARCHY = None
    UGEE_INST = None



    def __init__(self, name, description, valueType, setter, getter, formatter, nodeType=PROPT_SINGLE_GROUP, parent=None, multiget=None, multiget_expected=None):
        super().__init__(parent)
        self.__nodeProperties = Object()
        self.__nodeProperties.name = name
        self.__nodeProperties.description = description
        self.__nodeProperties.valueType = valueType
        self.__nodeProperties.nodeType = nodeType
        self.__nodeProperties.setter = setter
        self.__nodeProperties.getter = getter
        self.__nodeProperties.formatter = formatter
        self.__nodeProperties.multiget = multiget
        self.__nodeProperties.multiget_expected = multiget_expected



    #################
    # Node creation #
    #################
    @staticmethod
    def makeSingleAsMultiGroupResult(name, description, parent):
        return Prop(name, description, None, None, None, None, nodeType=PROPT_SINGLE_AS_MULTI_RESULT, parent=parent)

    @staticmethod
    def makeSingleGroup(name, description, parent, wasmulti=False):
        return Prop(name, description, None, None, None, None, nodeType=PROPT_SINGLE_GROUP, parent=parent)

    @staticmethod
    def makeMultiGroup(name, description, parent, multiget, multiget_expected):
        return Prop(name, description, None, None, None, None, nodeType=PROPT_MULTI_GROUP, parent=parent, multiget=multiget, multiget_expected=multiget_expected)

    @staticmethod
    def makeLeaf(name, description, parent, valueType, setter, getter, formatter):
        return Prop(name, description, valueType, setter, getter, formatter, nodeType=PROPT_LEAF, parent=parent)

    @staticmethod
    def makeRootNode():
        return Prop("", "", None, None, None, None, nodeType=PROPT_ROOT, parent=None)



    ##############################################
    # Node adding operations (used with grammar) #
    ##############################################
    def addSingleGroups(self, *groups):
        for g in groups:
            name, description = g
            hvp = Prop.makeSingleGroup(name, description, self)
            setattr(self, name, hvp)
            self.addChild(hvp)

    def addLeaves(self, *props):
        for p in props:
            name, description, valueType, setter, getter, formatter = p
            hvp = Prop.makeLeaf(name, description, self, valueType, setter, getter, formatter)
            setattr(self, name, hvp)
            self.addChild(hvp)

    def addMultiGroups(self, *mprops):
        for mp in mprops:
            name, description, multiget, multiget_exp = mp
            hvp = Prop.makeMultiGroup(name, description, self, multiget, multiget_exp)
            setattr(self, name, hvp)
            self.addChild(hvp)



    ####################
    # Info of the node #
    ####################
    def getName(self):
        return self.__nodeProperties.name

    def getDescription(self):
        return self.__nodeProperties.description

    def getValueType(self):
        return self.__nodeProperties.valueType

    def getNodeType(self):
        return self.__nodeProperties.nodeType

    def isSingleGroup(self):
        return self.__nodeProperties.nodeType == PROPT_SINGLE_GROUP

    def isMultiGroup(self):
        return self.__nodeProperties.nodeType == PROPT_MULTI_GROUP

    def isLeaf(self):
        return self.__nodeProperties.nodeType == PROPT_LEAF

    def isRoot(self):
        return self.__nodeProperties.nodeType == PROPT_ROOT

    def isSingleAsMultiGroupResult(self):
        return self.__nodeProperties.nodeType == PROPT_SINGLE_AS_MULTI_RESULT

    def getGetter(self):
        return self.__nodeProperties.getter

    def getSetter(self):
        return self.__nodeProperties.setter

    def getFormatter(self):
        return self.__nodeProperties.formatter

    def getMultiget(self):
        return self.__nodeProperties.multiget

    def getMultigetExpected(self):
        return self.__nodeProperties.multiget_expected

    def __str__(self):
        return "ROOT" if self.isRoot() else self.getName()

    def __repr__(self):
        return self.__str__()


    ##################
    # Children nodes #
    ##################
    def getChildByName(self, name):
        for i in self.getChildren():
            if i.getName() == name:
                return i
        return None

    def getChildByNameInsensitive(self, name):
        for i in self.getChildren():
            if str_equals_insensitive(i.getName(), name):
                return i
        return None

    def searchDescendeantsByPropPath(self, propPath):
        elements = self.__preVisit(True)
        nEls = len(elements)

        i = 0
        while i < nEls:
            currEl = elements[i]
            if not str_startswith_insensitive(currEl.getPropPath(), propPath):
                del elements[i]
                nEls -= 1
                i -= 1
            i += 1

        return elements


    def getAvailableLeaves(self):
        return self.__preVisit()


    def __preVisit(self, captureNodes=False):
        st = Stack()
        st.push(self)

        #print("ROOT IS: " + str(self))

        elements = []

        while not st.isEmpty():
            el = st.pop()
            if el.hasChildren():
                for i in list(reversed(el.getChildren())):
                    st.push(i)

                if captureNodes:
                    elements.append(el)

            else:
                elements.append(el)

        return elements



    ######################
    # Other getters/info #
    ######################
    def getParams(self):
        latest = self

        params = []

        while latest is not None:
            if latest.isSingleAsMultiGroupResult():
                params.append(latest.getName())
            latest = latest.getParent()

        return list(reversed(params))


    def getPropPath(self):
        latest = self

        available = []

        while not latest.isRoot():
            available.append(latest.getName())
            latest = latest.getParent()

        return ".".join(list(reversed(available)))


    def isDescendeantOf(self, node):
        latest = self

        while not latest.isRoot():
            parent = latest.getParent()
            if parent == node:
                return True
            latest = parent

        return False


    def isChildOf(self, node):
        return self.getParent() == node


    @staticmethod
    def setUgeeInst(ugeeInst):
        if Prop.UGEE_INST is None:
            Prop.UGEE_INST = ugeeInst
            generateHierarchy()



    @staticmethod
    def searchPropByPath(proppath):
        compnames = proppath.split(".")

        i = len(compnames) - 1
        while i >= 0:
            if compnames[i] == "":
                del compnames[i]
            i -= 1

        latest = Prop.HIERARCHY
        nonExistentTerritory = False
        nonExistents = []

        for i in compnames:
            #print(i)
            if not nonExistentTerritory:
                child = latest.getChildByNameInsensitive(i)
                if child is not None:
                    latest = child
                else:
                    nonExistents.append(i)
                    nonExistentTerritory = True
            else:
                nonExistents.append(i)

        return (latest, nonExistents,)



    @staticmethod
    def searchPropByPath2(proppath):
        compnames = proppath.split(".")

        i = len(compnames) - 1
        while i >= 0:
            if compnames[i] == "":
                del compnames[i]
            i -= 1

        latest = Prop.HIERARCHY
        nonExistentTerritory = False
        nonExistents = []

        for i in compnames:
            #print(i)
            if not nonExistentTerritory:
                child = latest.getChildByNameInsensitive(i)
                if child is not None:
                    latest = child
                else:
                    nonExistents.append(i)
                    nonExistentTerritory = True
            else:
                nonExistents.append(i)

        return (latest, nonExistents,)




    @staticmethod
    def __genDebugPrint(message, newline=True):
        if DEBUG_GENERATION:
            if not isinstance(message, str):
                message = str(message)

            printf(message + "\n" if newline else "")



    # Hierarchy generation
    @staticmethod
    def generateHierarchyFromGrammar():
        if Prop.HIERARCHY_GRAMMAR is not None:
            navStk = Stack()
            navStk.push(Prop.HIERARCHY_GRAMMAR)

            navChRemStk = Stack()
            navChRemStk.push(1)

            params = []

            creatRoot = Prop.makeRootNode()
            Prop.HIERARCHY = creatRoot
            creatLatest = creatRoot

            creatStk = Stack()
            creatStk.push((creatLatest, list(params), deepcopy(navStk), deepcopy(navChRemStk)))


            while not creatStk.isEmpty():
                latest = creatStk.pop()
                creatLatest, params, navStk, navChRemStk = latest

                Prop.__genDebugPrint("Restoring " + str(navStk) + ", creatLatest=" + str(creatLatest))

                while not navStk.isEmpty():
                    Prop.__genDebugPrint("nav: " + str(navStk))
                    navEl = navStk.pop()
                    Prop.__genDebugPrint("navEl: " + str(navEl))
                    Prop.__genDebugPrint("navChR: " + str(navChRemStk))
                    Prop.__genDebugPrint("params: " + str(params))
                    Prop.__genDebugPrint("creat: " + str(creatLatest))

                    # Update the list of available children, after extracting this one
                    remaining = navChRemStk.pop()

                    # Remove one from the remaining children, as the most recent one was popped
                    remaining -= 1
                    navChRemStk.push(remaining)

                    if navEl.hasChildren() and not navEl.isMultiGroup():
                        Prop.__handleMultiGroupWithChildren(navEl, navStk, navChRemStk)

                    if navEl.isMultiGroup():
                        Prop.__handleMultiGroup(navEl, navStk, navChRemStk, remaining, creatLatest, creatStk, params)
                        break

                    elif navEl.isSingleGroup():
                        Prop.__genDebugPrint("I AM SINGLE: " + str(navEl))
                        p = Prop.makeSingleGroup(navEl.getName(), navEl.getDescription(), creatLatest)
                        creatLatest.addChild(p)

                        if navEl.hasChildren():
                            creatLatest = p


                    elif navEl.isLeaf():
                        creatLatest = Prop.__handleLeaf(navEl, navChRemStk, remaining, creatLatest)

                    else:
                        Prop.__genDebugPrint("NO RECOGNIZED")


                    Prop.__genDebugPrint(navStk)




    @staticmethod
    def __handleMultiGroupWithChildren(navEl, navStk, navChRemStk):
        Prop.__genDebugPrint("I HAVE CHILDREN: \n")

        # Save the newest available children (number of them)

        noChildren = navEl.getNoChildren()
        navChRemStk.push(noChildren)

        # Push the actual children
        children = list(reversed(navEl.getChildren()))
        for i in children:
            navStk.push(i)

        Prop.__genDebugPrint("CHILDREN ADDED TO STACK\n")




    @staticmethod
    def __handleMultiGroup(navEl, navStk, navChRemStk, remaining, creatLatest, creatStk, params):
        Prop.__genDebugPrint("I AM MULTI: %s, %s\n" % (str(navEl), str(params)))

        # Preserve current analysis, we'll go back to it later
        preserveLatest = creatLatest
        if remaining == 0:
            # If this is the last of his siblings (=the last of his parent's children), we want to go upward BEFORE preserving, in order to properly construct the following remaining nodes
            navChRemStk.pop()
            preserveLatest = creatLatest.getParent()

        Prop.__genDebugPrint("Preserving current stack: " + str(navStk) + "; " + str(preserveLatest))
        creatStk.push((
            preserveLatest,
            list(params),
            deepcopy(navStk),
            deepcopy(navChRemStk),
        ))

        navStk.clear()
        children = list(reversed(navEl.getChildren()))
        for i in children:
            navStk.push(i)

        navChRemStk.clear()
        noChildren = navEl.getNoChildren()
        navChRemStk.push(noChildren)

        multiget = navEl.getMultiget()
        multigetExp = navEl.getMultigetExpected()
        multiNames = multigetExp(multiget(params))

        for i in list(multiNames):
            currParams = list(params)
            currParams.append(i)
            Prop.__genDebugPrint("Saving " + str(navStk) + " for " + i + ", rem=" + str(navChRemStk) + ", creat=" + str(creatLatest))
            p = Prop.makeSingleAsMultiGroupResult(i, navEl.getDescription(), creatLatest)
            creatStk.push((
                p,
                currParams,
                deepcopy(navStk),
                deepcopy(navChRemStk),
            ))
            creatLatest.addChild(p)




    @staticmethod
    def __handleLeaf(navEl, navChRemStk, remaining, creatLatest):
        p = Prop.makeLeaf(navEl.getName(), navEl.getDescription(), creatLatest, navEl.getValueType(), navEl.getSetter(), navEl.getGetter(), navEl.getFormatter())
        Prop.__genDebugPrint("I AM LEAF: " + str(navEl))
        Prop.__genDebugPrint("creatLatest: " + str(creatLatest))

        creatLatest.addChild(p)
        Prop.__genDebugPrint("NODE TYPE IS: " + str(p.getNodeType()))

        nUpwards = 0

        Prop.__genDebugPrint("remaining is :" + str(remaining))
        Prop.__genDebugPrint("nChS: " + str(navChRemStk))

        # Count how many times the hierarchy must go up (within parent in parent)
        navChRemStk.pop()
        while remaining == 0 and not navChRemStk.isEmpty():
            remaining = navChRemStk.pop()
            nUpwards += 1

        Prop.__genDebugPrint("nChE: " + str(navChRemStk))
        Prop.__genDebugPrint(nUpwards)


        # Restore the last available children (popped earlier, the first non-zero one)
        navChRemStk.push(remaining)

        Prop.__genDebugPrint("nChE2: " + str(navChRemStk))

        # Finally, move up in the hierarchy in the "construction node", so that future nodes, are correctly created at the right places
        i = 0
        while i < nUpwards and not creatLatest.isRoot():
            creatLatest = creatLatest.getParent()
            i += 1

        Prop.__genDebugPrint("KLCreateLatest: " + str(creatLatest))

        return creatLatest










from .propops import *






def generateGrammar():
    Prop.HIERARCHY_GRAMMAR = Prop.makeRootNode()
    Prop.HIERARCHY_GRAMMAR.addMultiGroups(
        (DEVICE_PROP_NAME, "Specific device", multiget_devices, multiget_devices_expected) #multiget_devices, multiget_devices_expected)
    )
    Prop.HIERARCHY_GRAMMAR.addSingleGroups(
        (DESKKEYS_PROP_NAME, "Desk keys settings",)
    )


    DEVICE_PROP = Prop.HIERARCHY_GRAMMAR.getChildByName(DEVICE_PROP_NAME)
    DESKKEYS_PROP = Prop.HIERARCHY_GRAMMAR.getChildByName(DESKKEYS_PROP_NAME)


    ###########################################
    # DEVICE.(pen|tablet|settings)
    DEVICE_PROP.addSingleGroups(
        ("pen", "The pen instrument"),
        ("tablet", "The tablet instrument"),
        ("settings", "The settings instrument"),
    )


    ###########################################
    # DEVICE.pen.(pressure|mousemode)
    DEVICE_PROP.pen.addSingleGroups(
        ("pressure", "The pen instrument"),
        ("mousemode", "The mousemode instrument"),
    )


    ###########################################
    # DEVICE.pen.tilt
    DEVICE_PROP.pen.addLeaves(
        ("tilt", "Is tilt detection enabled?", PTYPE_BOOLEAN, set_pentilt, get_pentilt, generic_formatter),
    )


    ###########################################
    # DEVICE.pen.(button<NUM>)
    DEVICE_PROP.pen.addMultiGroups(
        ("button", "Particular button", multiget_pen_buttons, multiget_pen_buttons_expected),
    )


    ###########################################
    # DEVICE.pen.pressure.(enabled|coords)
    DEVICE_PROP.pen.pressure.addLeaves(
        ("enabled", "Is pressure enabled?", PTYPE_BOOLEAN, set_penpressure, get_penpressure, generic_formatter),
        ("coords", "The three points used to detect pressure", PTYPE_PRESSURE, set_penpressure_points, get_penpressure_points, generic_formatter),
    )


    ###########################################
    # DEVICE.pen.mousemode.(enabled|speed)
    DEVICE_PROP.pen.mousemode.addLeaves(
        ("enabled", "Is relative mode enabled?", PTYPE_BOOLEAN, set_mousemode, get_mousemode, generic_formatter),
        ("speed", "Relative mode's speed (0 to 10)", PTYPE_INTEGER, set_mousemode_speed, get_mousemode_speed, generic_formatter),
    )


    ###########################################
    # DEVICE.pen.button<NUM>.(action_default)
    DEVICE_PROP.pen.button.addLeaves(
         ("action_default", "The default action (actid) for the button", PTYPE_DEFAULT_ACTION, multiple_pen_button_set_default_action, multiple_pen_button_get_default_action, actid_formatter),
    )


    ###########################################
    # DEVICE.pen.button<NUM>.(action_custom)
    DEVICE_PROP.pen.button.addSingleGroups(
        ("action_custom", "The custom action for the button",),
    )


    ###########################################
    # DEVICE.pen.button<NUM>.action_custom.(enabled|label|action)
    DEVICE_PROP.pen.button.action_custom.addLeaves(
        ("enabled", "Toggle to enable the use of the custom action", PTYPE_BOOLEAN, multiple_pen_button_set_custom_action_enabled, multiple_pen_button_get_custom_action_enabled, generic_formatter),
        ("label", "The label for the action", PTYPE_STRING, multiple_pen_button_set_custom_action_label, multiple_pen_button_get_custom_action_label, generic_formatter),
        ("action", "The actual custom action", PTYPE_CUSTOM_ACTION, multiple_pen_button_set_custom_action, multiple_pen_button_get_custom_action, generic_formatter),
    )


    ###########################################
    # DEVICE.tablet.(key|ring)
    DEVICE_PROP.tablet.addMultiGroups(
        ("key", "Settings related to the single tablet key", multiget_tablet_keys, multiget_tablet_keys_expected),
        ("ring", "Settings related to the single ring", multiget_tablet_rings, multiget_tablet_rings_expected)
    )


    ###########################################
    # DEVICE.tablet.(screenres|tabletres|tabletrot)
    DEVICE_PROP.tablet.addLeaves(
        ("screenres", "Rectangle representing the screen resolution", PTYPE_RECTANGLE, set_screenres, get_screenres, generic_formatter),
        ("tabletres", "Rectangle representing the tablet resolution", PTYPE_RECTANGLE, set_tabletres, get_tabletres, generic_formatter),
        ("tabletrot", "Settings related to the rotation of the tablet screen", PTYPE_INTEGER, set_tabletrot, get_tabletrot, generic_formatter),
    )


    ###########################################
    # DEVICE.tablet.key<NUM>.(action_default|action_custom)
    DEVICE_PROP.tablet.key.addLeaves(
        ("action_default", "The default action (actid) for the key", PTYPE_DEFAULT_ACTION, multiple_tablet_key_set_default_action, multiple_tablet_key_get_default_action, actid_formatter),
    )


    ###########################################
    # DEVICE.tablet.key<NUM>.(action_custom)
    DEVICE_PROP.tablet.key.addSingleGroups(
        ("action_custom", "The custom action for the key",),
    )


    ###########################################
    # DEVICE.tablet.key<NUM>.action_custom.(enabled|label|action)
    DEVICE_PROP.tablet.key.action_custom.addLeaves(
        ("enabled", "Toggle to enable the use of the custom action", PTYPE_BOOLEAN, multiple_tablet_key_set_custom_action_enabled, multiple_tablet_key_get_custom_action_enabled, generic_formatter),
        ("label", "The label for the action", PTYPE_STRING, multiple_tablet_key_set_custom_action_label, multiple_tablet_key_get_custom_action_label, generic_formatter),
        ("action", "The actual custom action", PTYPE_CUSTOM_ACTION, multiple_tablet_key_set_custom_action, multiple_tablet_key_get_custom_action, generic_formatter),
    )


    ###########################################
    # DEVICE.tablet.<RINGNAME>.(wheel_movement<NUM>)
    DEVICE_PROP.tablet.ring.addMultiGroups(
        ("wheel_movement", "Particular wheel movement", multiget_ring_wheel_movements, multiget_ring_wheel_movements_expected,),
    )


    ###########################################
    # DEVICE.tablet.<RINGNAME>.wheel_movement<NUM>.(usage|label|cw_label|ccw_label|ccw_action|cw_action)
    DEVICE_PROP.tablet.ring.wheel_movement.addLeaves(
        ("usage", "Toggle for enabling/defaulting/disabling the custom movement", PTYPE_INTEGER, multiple_ring_wheelmov_set_usage, multiple_ring_wheelmov_get_usage, generic_formatter),
        ("label", "The \"generic\" label for the action", PTYPE_STRING, multiple_ring_wheelmov_set_label, multiple_ring_wheelmov_get_label, generic_formatter),
        ("ccw_label", "The counter clockwise action's label", PTYPE_STRING, multiple_ring_wheelmov_set_custom_ccwaction_label, multiple_ring_wheelmov_get_custom_ccwaction_label, generic_formatter),
        ("cw_label", "The clockwise action's label", PTYPE_STRING, multiple_ring_wheelmov_set_custom_cwaction_label, multiple_ring_wheelmov_get_custom_cwaction_label, generic_formatter),
        ("ccw_action", "The counterclockwise action for the wheel", PTYPE_CUSTOM_ACTION, multiple_ring_wheelmov_set_custom_ccwaction, multiple_ring_wheelmov_get_custom_ccwaction, generic_formatter),
        ("cw_action", "The clockwise action for the wheel", PTYPE_CUSTOM_ACTION, multiple_ring_wheelmov_set_custom_cwaction, multiple_ring_wheelmov_get_custom_cwaction, generic_formatter),
    )


    ###########################################
    # DEVICE.settings.(messages|tabletkeys)
    DEVICE_PROP.settings.addLeaves(
        ("messages", "Toggle for showing messages", PTYPE_BOOLEAN, set_showmessages, get_showmessages, generic_formatter),
        ("tabletkeys", "Toggle for enabling/disabling tablet keys input", PTYPE_BOOLEAN, set_tabletkeys, get_tabletkeys, generic_formatter),
    )


    ###########################################
    # DESKKEYS.(fixed|zoom|nokeys)
    DESKKEYS_PROP.addLeaves(
        ("fixed", "Toggle for fixed/movable desk keys window", PTYPE_BOOLEAN, set_deskkeys_fixed, get_deskkeys_fixed, generic_formatter),
        ("zoom", "Desk keys window zoom", PTYPE_FLOAT, set_deskkeys_zoom, get_deskkeys_zoom, generic_formatter),
        ("nokeys", "Number of keys to use", PTYPE_INTEGER, set_deskkeys_nokeys, get_deskkeys_nokeys, generic_formatter)
    )


    ###########################################
    # DESKKEYS.(vkey<NUM>)
    DESKKEYS_PROP.addMultiGroups(
        ("vkey", "Particular (virtual) desk key", multiget_deskkeys_vkeys, multiget_deskkeys_vkeys_expected,)
    )

    ###########################################
    # DESKKEYS.(vkey<NUM>).(action_default|action_custom)
    DESKKEYS_PROP.vkey.addLeaves(
        ("action_default", "The default action (actid) for the button", PTYPE_DEFAULT_ACTION, multiple_deskkeys_vkeys_set_default_action, multiple_deskkeys_vkeys_get_default_action, actid_formatter),
    )

    ###########################################
    # DESKKEYS_PROP.vkey<NUM>.(action_custom)
    DESKKEYS_PROP.vkey.addSingleGroups(
        ("action_custom", "The custom action for the virtual key",),
    )

    ###########################################
    # DESKKEYS_PROP.vkey<NUM>.action_custom.(action|name)
    DESKKEYS_PROP.vkey.action_custom.addLeaves(
        ("enabled", "Toggle to enable the use of the custom action", PTYPE_BOOLEAN, multiple_deskkeys_vkeys_set_custom_action_enabled, multiple_deskkeys_vkeys_get_custom_action_enabled, generic_formatter),
        ("label", "The label for the action", PTYPE_STRING, multiple_deskkeys_vkeys_set_custom_action_label, multiple_deskkeys_vkeys_get_custom_action_label, generic_formatter),
        ("action", "The actual custom action", PTYPE_CUSTOM_ACTION, multiple_deskkeys_vkeys_set_custom_action, multiple_deskkeys_vkeys_get_custom_action, generic_formatter),
    )







def generateHierarchy():
    # Generate grammar
    generateGrammar();

    # Generate actual hierarchy
    Prop.generateHierarchyFromGrammar()
