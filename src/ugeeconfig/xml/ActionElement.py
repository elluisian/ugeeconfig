import re
import os


from ..utils.XMLElement import *
from ..utils.utils import *
from ..data.Action import *



# Used to verify the correctness of the format of a single action
REGEX_AVAILABLE_ACTION_TYPES = "^(1|2|3|4|5|6|7|10)$"
REGEX_ACTION_KEYSTROKE_FORMAT = "([0-9]+:[0-9](+[0-9]+:[0-9]+)*(,[0-9]+:[0-9](+[0-9]+:[0-9]+)*)*)|"
REGEX_ACTION_MOUSEKEY_FORMAT = "([0-9]+(+[0-9]+)*)|"
REGEX_ACTION_SINGLE_ACTID_FORMAT = "([0-9]+)|"



class ActionElementException(Exception):
    def __init__(self, message):
        super.__init__(message)



class ActionElement(XMLElement):
    def __init__(self, customActionDataInst):
        self.customActionDataInst = customActionDataInst


    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        dataObj = ActionElement.__parseActionData(elem.text)

        if isinstance(self.customActionDataInst, WheelCustomActionData):
            self.customActionDataInst.setLabel(dataObj.label)
            self.customActionDataInst.setCWLabel(dataObj.cwlabel)
            self.customActionDataInst.setCCWLabel(dataObj.ccwlabel)
            self.customActionDataInst.setCWAction(dataObj.cwActInst)
            self.customActionDataInst.setCCWAction(dataObj.ccwActInst)
            return None

        else:
            actInst = dataObj.actInst
            self.customActionDataInst.setLabel(dataObj.label)

        return actInst





    @staticmethod
    def __parseActionData(contents, actSz):
        actionData = str(contents)
        actionData = actionData.split("|")
        actSz = len(actionData)

        dataObj = Object()
        dataObj.label = ""
        dataObj.actInst = UnsetCAction.INSTANCE

        if actSz == 1 and actionData[0] == "":
            return dataObj

        if not re.match(REGEX_AVAILABLE_ACTION_TYPES, actionData[0]):
            raise ActionElementException("XML read error: Invalid type of action \"%s\"" % (actionData[0],))

        actType = int(actionData[0])
        if actType in (ACTION_TYPE_KEYSTROKE, ACTION_TYPE_MOUSE, ACTION_TYPE_FUNCTION, ACTION_TYPE_EXEC, ACTION_TYPE_SYSOP, ACTION_TYPE_MULTIMEDIA,):
            if actSz != 4:
                raise ActionElementException("XML read error: Invalid number of arguments for action type %d (%d, %d expected" % (actType, actSz, 4,))

            dataObj.label = actionData[2]
            contents = actionData[3]

            if actType == ACTION_TYPE_KEYSTROKE:
                if not re.match(REGEX_ACTION_KEYSTROKE_FORMAT, contents):
                    raise ActionElementException("XML read error: Invalid action for type KEYSTROKE \"%s\"" % (contents,))
                dataObj.actInst = KeysAction(ActionElement.__readKeystrokes(contents))

            elif actType == ACTION_TYPE_MOUSE:
                if not re.match(REGEX_ACTION_MOUSEKEY_FORMAT, contents):
                    raise ActionElementException("XML read error: Invalid action for type MOUSE \"%s\"" % (contents,))
                dataObj.actInst = MouseAction(ActionElement.__readMouse(contents))

            elif actType == ACTION_TYPE_EXEC:
                dataObj.actInst =  ExecAction(ActionElement.__readExec(contents))

            elif actType == ACTION_TYPE_FUNCTION:
                if not re.match(REGEX_ACTION_SINGLE_ACTID_FORMAT, contents):
                    raise ActionElementException("XML read error: Invalid action for type FUNCTION \"%s\"" % (contents,))
                dataObj.actInst =  FunctionAction(ActionElement.__readActid(contents))

            elif actType == ACTION_TYPE_SYSOP:
                if not re.match(REGEX_ACTION_SINGLE_ACTID_FORMAT, contents):
                    raise ActionElementException("XML read error: Invalid action for type SYSOP \"%s\"" % (contents,))
                dataObj.actInst = SysopAction(ActionElement.__readActid(contents))

            elif actType == ACTION_TYPE_MULTIMEDIA:
                if not re.match(REGEX_ACTION_SINGLE_ACTID_FORMAT, contents):
                    raise ActionElementException("XML read error: Invalid action for type MULTIMEDIA \"%s\"" % (contents,))
                dataObj.actInst = MultimediaAction(ActionElement.__readActid(contents))

        elif actType == ACTION_TYPE_NONE:
            if actSz != 3:
                raise ActionElementException("XML read error: Invalid number of arguments for action type NONE (%d, %d expected" % (actSz, 3,))
            dataObj.actInst = NopCAction.INSTANCE

        elif actType == ACTION_WHEELMOVE:
            dataObj.label = actionData[1]
            dataObj.ccwlabel = actionData[2]
            dataObj.cwlabel = actionData[2]
            cwkeystrokes = actionData[3]
            ccwkeystrokes = actionData[4]

            if not re.match(REGEX_ACTION_KEYSTROKE_FORMAT, cwkeystrokes):
                raise ActionElementException("XML read error: Invalid action for type KEYSTROKE \"%s\" (CW keystrokes)" % (cwkeystrokes,))

            if not re.match(REGEX_ACTION_KEYSTROKE_FORMAT, ccwkeystrokes):
                raise ActionElementException("XML read error: Invalid action for type KEYSTROKE \"%s\" (CCW keystrokes)" % (cwkeystrokes,))

            dataObj.cwkeystrokes = KeysAction(ActionElement.__readKeystrokes(cwkeystrokes))
            dataObj.cwkeystrokes = KeysAction(ActionElement.__readKeystrokes(ccwkeystrokes))


        return dataObj





    @staticmethod
    def __readKeystrokes(contents):
        keystrLsToRead = values.split(",")
        keystrLs = []

        for kstrgrp in keystrLsToRead:
            keystrkInst = Keystroke()
            keystrLs.append(keystrkInst)

            sKeys = kstrgrp.split("+")
            for skey in sKeys:
                keysym, keycode = skey.split(":")
                keystrkInst.addKey(SingleKey.fromKeysymCode(xmint_to_int(keysym), xmint_to_int(keycode),))


        return keystrLs


    @staticmethod
    def __readMouse(contents):
        mkeysLsToRead = values.split("+")
        mKeysLs = []

        for mk in mkeysLs:
            mKeysLs.append(SingleActid.makeMouseKey(xmint_to_int(mk)))

        return mKeysLs


    @staticmethod
    def __readExec(contents):
        return contents
        #if os.path.exists(contents) and not os.path.isdir(contents):
        #    return contents
        #raise ActionElementException("XML read error: path \"%s\" is not valid!" % (contents,))


    @staticmethod
    def __readActid(actType, contents):
        actid = xmint_to_int(contents)

        if (actType == ACTION_TYPE_FUNCTION and not ACTID_FUNCT_DISPIFACE <= actid <= ACTID_FUNCT_DESKKEYS) or\
          (actType == ACTION_TYPE_SYSOP and not ACTID_SYSOP_LOCKSCR <= actid <= ACTID_SYSOP_STARTMENU) or\
          (actType == ACTION_TYPE_MULTIMEDIA and not ACTID_MULTIM_PREV <= actid <= ACTID_MULTIM_MUTE):
            raise ActionElementException("XML read error: invalid actid value \"%d\"!" % (actid,))

        return actid




    def writeToElement(self, data, parent=None):
        if parent is None:
            raise InvalidXMLTag("Parent is None!")

        actInst = data
        actType = self.customActionDataInst.getActionType()
        actLabel = self.customActionDataInst.getLabel()

        element = None

        if actType == ACTION_TYPE_KEYSTROKE:
            element = "%d||%s|%s" % (actType, actLabel, ActionElement.__writeKeystrokes(actInst.getKeystrokes()),)

        elif actType == ACTION_TYPE_MOUSE:
            element = "%d||%s|%s" % (actType, actLabel, ActionElement.__writeMouse(actInst.getMKeys()),)

        elif actType in (ACTION_TYPE_FUNCTION, ACTION_TYPE_SYSOP, ACTION_TYPE_MULTIMEDIA):
            element = "%d||%s|%d" % (actType, actLabel, ActionElement.__writeActid(actInst.getActidData()),)

        elif actType == ACTION_TYPE_EXEC:
            element = "%d||%s|%s" % (actType, actLabel, ActionElement.__writeExec(actInst.getPath()))

        elif actType == ACTION_TYPE_NONE:
            element = "%d|%s|%s" % (actType, actLabel, actLabel)

        elif actType == ACTION_TYPE_WHEELMOVE:
            isSet = self.customActionDataInst.isCWActionSet() or self.customActionDataInst.isCCWActionSet()

            if isSet:
                cwActInst = self.customActionDataInst.getCWAction()
                ccwActInst = self.customActionDataInst.getCCWAction()

                genLabel = "" if actLabel is None else actLabel
                ccwLabel = self.customActionDataInst.getCCWLabel()
                ccwLabel = "" if ccwLabel is None else ccwLabel
                cwLabel = self.customActionDataInst.getCWLabel()
                cwLabel = "" if ccwLabel is None else ccwLabel
                ccwKeystrokes = ActionElement.__writeKeystrokes(ccwActInst.getKeystrokes()) if ccwActInst is not None else ""
                cwKeystrokes = ActionElement.__writeKeystrokes(cwActInst.getKeystrokes()) if cwActInst is not None else ""
                usage = self.customActionDataInst.getUsage()

                element = "%d|%s|%s|%s|%s|%s" % (actType, genLabel, ccwLabel, cwLabel, ccwKeystrokes, cwKeystrokes)

                parent.text = element

                if usage == WheelCustomActionData.USAGE_DEFAULT:
                    usage = 0
                elif usage == WheelCustomActionData.USAGE_DEFAULT:
                    usage = 1
                elif usage == WheelCustomActionData.USAGE_NOP:
                    usage = 2

                parent.attrib["id"] = str(usage)

                return element



    @staticmethod
    def __writeKeystrokes(keystrokes):
        kstrkLs = []

        for keystrk in keystrokes:
            kLs = []
            for i in range(0, keystrk.getKeyNo()):
                k = keystrk.getKey(i)
                kLs.append("%d:%d" % (k.getKeysym(), k.getKeycode(),))

            kstrkLs.append("+".join(kLs))

        return ",".join(kstrkLs)


    @staticmethod
    def __writeMouse(mousekeys):
        klist = []
        print(mousekeys)
        print(type(mousekeys[0]))
        for mkey in mousekeys:
            klist.append(str(mkey.getActid()))

        return "+".join(klist)


    @staticmethod
    def __writeActid(actidInst):
        return actidInst.getActid()


    @staticmethod
    def __writeExec(contents):
        if os.path.exists(contents) and not os.path.isdir(contents):
            return str(contents)

        raise ActionElementException("ERROR")