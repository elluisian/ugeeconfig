from abc import ABC, abstractmethod


from ..utils.utils import str_equals_insensitive
from ..utils.AugmentedXK import Xlib



# Action types
ACTION_TYPE_KEYSTROKE = 1
ACTION_TYPE_MOUSE = 2
ACTION_TYPE_FUNCTION = 3
ACTION_TYPE_WHEELMOVE = 4
ACTION_TYPE_EXEC = 5
ACTION_TYPE_SYSOP = 6
ACTION_TYPE_MULTIMEDIA = 7
ACTION_TYPE_NONE = 10
ACTION_TYPE_NOT_SET = 11




# Actids
ACTID_DRV_PENERSR = 1
ACTID_DRV_MOUSEK = 2
ACTID_DRV_KEYSTROKE = 3
ACTID_DRV_DEVICE = 4
ACTID_DRV_RUNAPP = 5
ACTID_DRV_SYSOP = 6
ACTID_DRV_MULTIMEDIA = 7
ACTID_DRV_NOP = 10
ACTID_DRV_CUSTOMIZE = 11
ACTID_DRV_DEFAULT = 12
ACTID_DRV_TYPE = "actid_drv"
ACTID_DRV_VALUES = (
    ACTID_DRV_PENERSR,
    ACTID_DRV_MOUSEK,
    ACTID_DRV_KEYSTROKE,
    ACTID_DRV_DEVICE,
    ACTID_DRV_RUNAPP,
    ACTID_DRV_SYSOP,
    ACTID_DRV_MULTIMEDIA,
    ACTID_DRV_NOP,
    ACTID_DRV_CUSTOMIZE,
    ACTID_DRV_DEFAULT,
)



ACTID_MOUSEK_SHIFT = 201
ACTID_MOUSEK_LALT = 202
ACTID_MOUSEK_RALT = 203
ACTID_MOUSEK_CTRL = 204
ACTID_MOUSEK_SPACE = 205
ACTID_MOUSEK_LCLICK = 206
ACTID_MOUSEK_RCLICK = 207
ACTID_MOUSEK_SCLICK = 208
ACTID_MOUSEK_LDCLICK = 209
ACTID_MOUSEK_SCRUP = 210
ACTID_MOUSEK_SCRDOWN = 211
ACTID_MOUSEK_TYPE = "actid_mousek"
ACTID_MOUSEK_VALUES = (
    ACTID_MOUSEK_SHIFT,
    ACTID_MOUSEK_LALT,
    ACTID_MOUSEK_RALT,
    ACTID_MOUSEK_CTRL,
    ACTID_MOUSEK_SPACE,
    ACTID_MOUSEK_LCLICK,
    ACTID_MOUSEK_RCLICK,
    ACTID_MOUSEK_SCLICK,
    ACTID_MOUSEK_LDCLICK,
    ACTID_MOUSEK_SCRUP,
    ACTID_MOUSEK_SCRDOWN,
)



ACTID_KEYSTRK_B = 301
ACTID_KEYSTRK_E = 302
ACTID_KEYSTRK_ALT = 303
ACTID_KEYSTRK_SPACE = 304
ACTID_KEYSTRK_CTRLS = 305
ACTID_KEYSTRK_CTRLZ = 306
ACTID_KEYSTRK_CTRLALTZ = 307
ACTID_KEYSTRK_CTRLSHIFTZ = 308
ACTID_KEYSTRK_V = 309
ACTID_KEYSTRK_L = 310
ACTID_KEYSTRK_CTRLO = 311
ACTID_KEYSTRK_CTRLN = 312
ACTID_KEYSTRK_CTRLSHIFTN = 313
ACTID_KEYSTRK_CTRLE = 314
ACTID_KEYSTRK_F = 315
ACTID_KEYSTRK_D = 316
ACTID_KEYSTRK_X = 317
ACTID_KEYSTRK_CTRLDEL = 318
ACTID_KEYSTRK_CTRLC = 319
ACTID_KEYSTRK_CTRLV = 320
ACTID_KEYSTRK_CTRLPLUS = 321
ACTID_KEYSTRK_CTRLMINUS = 322
ACTID_KEYSTRK_TAB = 323
ACTID_KEYSTRK_F5 = 324
ACTID_KEYSTRK_CLBRK = 325
ACTID_KEYSTRK_OPBRK = 326
ACTID_KEYSTRK_CTRLCLBRK = 327
ACTID_KEYSTRK_CTRLOPBRK = 328 #ACTID_KEYSTRK_CTRLOPBRKN = 328
ACTID_KEYSTRK_TYPE = "actid_keystrk"
ACTID_KEYSTRK_VALUES = (
    ACTID_KEYSTRK_B,
    ACTID_KEYSTRK_E,
    ACTID_KEYSTRK_ALT,
    ACTID_KEYSTRK_SPACE,
    ACTID_KEYSTRK_CTRLS,
    ACTID_KEYSTRK_CTRLZ,
    ACTID_KEYSTRK_CTRLALTZ,
    ACTID_KEYSTRK_CTRLSHIFTZ,
    ACTID_KEYSTRK_V,
    ACTID_KEYSTRK_L,
    ACTID_KEYSTRK_CTRLO,
    ACTID_KEYSTRK_CTRLN,
    ACTID_KEYSTRK_CTRLSHIFTN,
    ACTID_KEYSTRK_CTRLE,
    ACTID_KEYSTRK_F,
    ACTID_KEYSTRK_D,
    ACTID_KEYSTRK_X,
    ACTID_KEYSTRK_CTRLDEL,
    ACTID_KEYSTRK_CTRLC,
    ACTID_KEYSTRK_CTRLV,
    ACTID_KEYSTRK_CTRLPLUS,
    ACTID_KEYSTRK_CTRLMINUS,
    ACTID_KEYSTRK_TAB,
    ACTID_KEYSTRK_F5,
    ACTID_KEYSTRK_CLBRK,
    ACTID_KEYSTRK_OPBRK,
    ACTID_KEYSTRK_CTRLCLBRK,
    ACTID_KEYSTRK_CTRLOPBRK,
)



ACTID_FUNCT_DISPIFACE = 401
ACTID_FUNCT_SWITCHMON = 402
ACTID_FUNCT_PENERSR = 403
ACTID_FUNCT_PRECMODE = 404
ACTID_FUNCT_SWRING1 = 405
ACTID_FUNCT_SWRING2 = 406
ACTID_FUNCT_TRACKMODE = 407
ACTID_FUNCT_BE = 408
ACTID_FUNCT_ERSR = 409
ACTID_FUNCT_DESKKEYS = 410
ACTID_FUNCT_TYPE = "actid_funct"
ACTID_FUNCT_VALUES = (
    ACTID_FUNCT_DISPIFACE,
    ACTID_FUNCT_SWITCHMON,
    ACTID_FUNCT_PENERSR,
    ACTID_FUNCT_PRECMODE,
    ACTID_FUNCT_SWRING1,
    ACTID_FUNCT_SWRING2,
    ACTID_FUNCT_TRACKMODE,
    ACTID_FUNCT_BE,
    ACTID_FUNCT_ERSR,
    ACTID_FUNCT_DESKKEYS,
)



ACTID_SYSOP_LOCKSCR = 601
ACTID_SYSOP_SHUTDOWN = 602
ACTID_SYSOP_HIBERNATE = 603
ACTID_SYSOP_SHOWACTS = 604
ACTID_SYSOP_STARTMENU = 605
ACTID_SYSOP_TYPE = "actid_sysop"
ACTID_SYSOP_VALUES = (
    ACTID_SYSOP_LOCKSCR,
    ACTID_SYSOP_SHUTDOWN,
    ACTID_SYSOP_HIBERNATE,
    ACTID_SYSOP_SHOWACTS,
    ACTID_SYSOP_STARTMENU,
)



ACTID_MULTIM_PREV = 701
ACTID_MULTIM_NEXT = 702
ACTID_MULTIM_TOGPPS = 703
ACTID_MULTIM_VOLPLUS = 704
ACTID_MULTIM_VOLMINUS = 705
ACTID_MULTIM_MUTE = 706
ACTID_MULTIM_TYPE = "actid_multim"
ACTID_MULTIM_VALUES = (
    ACTID_MULTIM_PREV,
    ACTID_MULTIM_NEXT,
    ACTID_MULTIM_TOGPPS,
    ACTID_MULTIM_VOLPLUS,
    ACTID_MULTIM_VOLMINUS,
    ACTID_MULTIM_MUTE,
)




class ActionException(Exception):
    def __init__(self, message):
        super().__init__(message)






class CustomActionData(object):
    def __init__(self):
        # Please note that if an action is set, it doesn't mean that it is enabled
        # In particular, if enabled = False, it means that the action is stored, but not used.
        self.actType = ACTION_TYPE_NOT_SET  # Is it set?
        self.label = None
        self.enabled = False # Is it enabled?
        self.action = None

    def isEnabled(self):
        return self.enabled

    def setEnabled(self, v):
        self.enabled = v

    def getActionType(self):
        return self.actType

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def setAction(self, action):
        if isinstance(action, UnsetCAction):
            self.actType = ACTION_TYPE_NOT_SET
            self.action = None

        elif isinstance(action, NopCAction):
            self.actType = ACTION_TYPE_NOP
            self.action = NopCAction.INSTANCE

        elif isinstance(action, KeysAction):
            self.actType = ACTION_TYPE_KEYSTROKE
            self.action = action

        elif isinstance(action, MouseAction):
            self.actType = ACTION_TYPE_MOUSE
            self.action = action

        elif isinstance(action, ExecAction):
            self.actType = ACTION_TYPE_EXEC
            self.action = action

        elif isinstance(action, FunctionAction):
            self.actType = ACTION_TYPE_FUNCTION
            self.action = action

        elif isinstance(action, SysopAction):
            self.actType = ACTION_TYPE_SYSOP
            self.action = action

        elif isinstance(action, MultimediaAction):
            self.actType = ACTION_TYPE_MULTIMEDIA
            self.action = action

    def getAction(self):
        return self.action

    def isActionSet(self):
        return self.actType


    def __deepcopy__(self, m):
        inst = CustomActionData()
        inst.actType = self.actType
        inst.label = self.label
        inst.enabled = self.enabled
        inst.action = self.action
        return inst



WHEEL_USG_DEFAULT = "usg_default"
WHEEL_USG_CUSTOM = "usg_custom"
WHEEL_USG_NOP = "usg_nop"

class WheelCustomActionData(object):
    def __init__(self):
        self.label = None
        self.usage = WHEEL_USG_DEFAULT
        self.cwlabel = None
        self.ccwlabel = None
        self.cwaction = None
        self.ccwaction = None


    def getUsage(self):
        return self.usage

    def setUsage(self, usage):
        self.usage = usage

    def getActionType(self):
        return ACTION_TYPE_WHEELMOVE

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getCWLabel(self):
        return self.cwlabel

    def setCWLabel(self, cwlabel):
        self.cwlabel = cwlabel

    def getCCWLabel(self):
        return self.ccwlabel

    def setCCWLabel(self, cwlabel):
        self.cwlabel = ccwlabel

    def setCWAction(self, cwaction):
        if not isinstance(cwaction, KeysAction):
            raise Exception("error: needed KeysAction!")
        self.cwaction = cwaction

    def getCWAction(self):
        return self.cwaction

    def setCCWAction(self, ccwaction):
        if not isinstance(ccwaction, KeysAction):
            raise Exception("error: needed KeysAction!")
        self.ccwaction = ccwaction

    def getCCWAction(self):
        return self.ccwaction

    def isCWActionSet(self):
        return self.cwaction is not None

    def isCCWActionSet(self):
        return self.ccwaction is not None


    def __deepcopy__(self, m):
        inst = WheelCustomActionData()
        inst.label = self.label
        inst.usage = self.usage
        inst.cwlabel = self.cwlabel
        inst.ccwlabel = self.ccwlabel
        inst.cwaction = self.cwaction
        inst.ccwaction = self.ccwaction
        return inst




class CustomAction(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __deepcopy__(self, m):
        pass



class UnsetCAction(CustomAction):
    INSTANCE = None
    def __init__(self):
        super().__init__()

    def __deepcopy__(self, m):
        return self

UnsetCAction.INSTANCE = UnsetCAction()



class NopCAction(CustomAction):
    INSTANCE = None
    def __init__(self):
        super().__init__()

    def __deepcopy__(self, m):
        return self

NopCAction.INSTANCE = NopCAction()












class SingleKey(object):
    def __init__(self, keysym, keycode):
        self.keysym = keysym
        self.keycode = keycode
        self.keyname = Xlib.XK.get_augmented_keyname(self.keysym)

    def getKeyname(self):
        return self.keyname

    def getKeysym(self):
        return self.keysym

    def getKeycode(self):
        return self.keycode

    @staticmethod
    def fromKeysymCode(keysym, keycode):
        return SingleKey(keysym, keycode)

    @staticmethod
    def fromKeyName(keyname):
        keydata = Xlib.XK.get_augmented_keysym_keycode(keyname)
        if keydata is not None:
            return SingleKey(keydata[0], keydata[1])

        return None

    def __str__(self):
        return "%s:%s:%s" % (self.getKeysym(), self.getKeycode(), self.getKeyname(),)

    def __deepcopy__(self, m):
        keysym = self.keysym
        keycode = self.keycode
        return SingleKey(keysym, keycode)



class Keystroke(object):
    def __init__(self):
        self.keys = []
        self.keysNo = 0

    def addKey(self, key):
        self.keys.append(key)
        self.keysNo += 1

    def getKey(self, idx):
        if 0 <= idx < self.keysNo:
            return self.keys[idx]

        return None

    def getKeyNo(self):
        return self.keysNo

    def __str__(self):
        return str(self.keys)

    def __deepcopy__(self, m):
        inst = Keystroke()
        inst.keys = list(map(lambda x : deepcopy(x), self.keys))
        inst.keysNo = len(inst.keys)
        return inst



class KeysAction(CustomAction):
    def __init__(self, keystrokeLs):
        self.keystrokeLs = list(keystrokeLs)
        self.keystrokeLsNo = len(self.keystrokeLs)

    def getKeystroke(self, idx):
        if 0 <= idx < self.keystrokeLsNo:
            return self.keystrokeLs[idx]

        return None

    def getKeystrokeNo(self):
        return self.keystrokeLsNo

    def getKeystrokes(self):
        return list(self.keystrokeLs)

    def __deepcopy__(self, m):
        return KeysAction(list(map(lambda x : deepcopy(x), self.getKeystrokes())))




class SingleActid(object):
    def __init__(self, actid):
        self.actid = actid
        self.actidname = getActIdFromValue(actid)

    def getActid(self):
        return self.actid

    def getActidName(self):
        return self.actidname

    @staticmethod
    def fromActid(actid, validGroup, groupType):
        isStr = isinstance(actid, str)

        actiddata = getActIdFromValue(actid)

        if actiddata is not None:
            if actiddata[1] in validGroup:
                return SingleActid(actiddata[1])

        if actiddata is None:
            excpMessage = "Error during single actid creation, %s \"%s\" is not a valid actid for group \"%s\"!" % (
                "string" if isStr else "integer", str(actid), str(groupType),
            )
        else:
            excpMessage = "Error during single actid creation, actid \"%d (%s)\" is not a valid actid for group \"%s\"!" % (
                actiddata[1], actiddata[0], groupType,
            )
        raise ActionException(excpMessage)

    def __deepcopy__(self, m):
        return SingleActid(self.getActid())



class MouseAction(CustomAction):
    def __init__(self, mkeys):
        self.mkeys = list(mkeys)
        self.mkeysNo = len(self.mkeys)

    def getMKey(self, idx):
        if 0 <= idx < self.mkeysNo:
            return self.mkeys[idx]

        return None

    def getMKeyNo(self):
        return self.mkeysNo

    def getMKeys(self):
        return list(self.mkeys)

    def __deepcopy__(self, m):
        mkeys = list(map(lambda x : deepcopy(x), self.getMKeys()))
        return MouseAction(mkeys)




class ExecAction(CustomAction):
    def __init__(self, fpath):
        self.fpath = fpath

    def getPath(self):
        return self.fpath

    def __deepcopy__(self, m):
        return ExecAction(self.fpath)



class ActidCustomAction(CustomAction):
    def __init__(self, singleactidinst):
        self.singleactidinst = singleactidinst

    def getActidData(self):
        return self.singleactidinst

    @abstractmethod
    def __deepcopy__(self, m):
        pass



class FunctionAction(ActidCustomAction):
    def __init__(self, singleactidinst):
        super().__init__(singleactidinst)

    def __deepcopy__(self, m):
        return FunctionAction(self.singleactidinst)


class SysopAction(ActidCustomAction):
    def __init__(self, singleactidinst):
        super().__init__(singleactidinst)

    def __deepcopy__(self, m):
        return SysopAction(self.singleactidinst)


class MultimediaAction(ActidCustomAction):
    def __init__(self, singleactidinst):
        super().__init__(singleactidinst)

    def __deepcopy__(self, m):
        return MultimediaAction(self.singleactidinst)





def getAvailableActIds():
    kl = globals()
    actid_mnem = []
    actid_value = []
    for i in kl.keys():
        if i.startswith("ACTID_"):
            filtered = i[len("ACTID_"):]
            if filtered.startswith("DRV_"):
                if filtered != "DRV_NOP":
                    continue

            # Exclude the group of values
            if filtered.endswith("_VALUES") or filtered.endswith("_TYPE"):
                continue

            actid_mnem.append(filtered)
            actid_value.append(kl[i])

    return (actid_mnem, actid_value,)




def getActIdFromValue(val):
    actiddata = getAvailableActIds()

    toRet = None

    isStr = isinstance(val, str)
    szLs = len(actiddata[0])

    for idx in range(0, szLs):
        if isStr and str_equals_insensitive(val, actiddata[0][idx]):
            toRet = (actiddata[0][idx], actiddata[1][idx])
            break

        elif val == actiddata[1][idx]:
            toRet = (actiddata[0][idx], actiddata[1][idx])
            break

    #print("toRet is: " + str(toRet))

    return toRet