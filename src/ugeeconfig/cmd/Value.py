import re


from .valueparser.ValueParser import *
from ..data.PressurePoints import *
from ..utils.Rectangle import *


PTYPE_BOOLEAN = "boolean"
PTYPE_INTEGER = "integer"
PTYPE_FLOAT = "float"
PTYPE_RECTANGLE = "rectangle"
PTYPE_PRESSURE = "pressure"
PTYPE_DEFAULT_ACTION = "default_action"
PTYPE_CUSTOM_ACTION = "custom_action"
PTYPE_STRING = "string"



# A single value that can be passed for a single prop on the command line
class Value(object):
    def __init__(self, value):
        self.v = None
        self.type = None

        elems = []
        elemSz = 0

        try:
            valparser = ValueParser(value)
            elems = valparser.parse()
            elemSz = len(elems)

        except ValueParserException as ex:
            self.type = PTYPE_STRING
            self.v = str(value)
            return


        if elemSz == 0:
            self.type = PTYPE_STRING
            self.v = str(value)
            return


        t = elems[0]
        tType = t.getTokenType()
        tVal = t.getTokenValue()

        if Value.__isTokenBoolean(tType):
            self.type = PTYPE_BOOLEAN
            self.v = tType == TOKEN_TRUE

        elif Value.__isTokenInteger(tType):
            self.type = PTYPE_INTEGER
            self.v = Value.__makeInteger(tVal)

        elif tType == TOKEN_RECTANGLE:
            self.type = PTYPE_RECTANGLE
            v1 = Value.__makeInteger(elems[1].getTokenValue())
            v2 = Value.__makeInteger(elems[3].getTokenValue())
            v3 = Value.__makeInteger(elems[5].getTokenValue())
            v4 = Value.__makeInteger(elems[7].getTokenValue())
            self.v = Rectangle(v1, v2, v3, v4)

        elif tType == TOKEN_PRESSURE:
            self.type = PTYPE_PRESSURE
            v1 = Value.__makeFloat(elems[1].getTokenValue())
            v2 = Value.__makeFloat(elems[3].getTokenValue())
            v3 = Value.__makeFloat(elems[5].getTokenValue())
            v4 = Value.__makeFloat(elems[7].getTokenValue())
            self.v = PressurePoints.fromValues(v1, v2, v3, v4)

        elif Value.__isTokenCustomAction(tType):
            self.type = PTYPE_CUSTOM_ACTION

            if tType == TOKEN_KEYS:
                self.v = KeysAction(Value.__collectKeystrokes(elems[1:]))

            elif tType == TOKEN_MOUSE:
                self.v = MouseAction(Value.__collectMouseKeys(elems[1:]))

            elif tType == TOKEN_FUNCT:
                self.v = FunctionAction(Value.__collectSingleActid(elems[1], ACTID_FUNCT_VALUES, ACTID_FUNCT_TYPE))

            elif tType == TOKEN_EXEC:
                self.v = ExecAction(elem[1])

            elif tType == TOKEN_SYSOP:
                self.v = SysopAction(Value.__collectSingleActid(elems[1], ACTID_SYSOP_VALUES, ACTID_SYSOP_TYPE))

            elif tType == TOKEN_MULTIMEDIA:
                self.v = MultimediaAction(Value.__collectSingleActid(elems[1], ACTID_MULTIM_VALUES, ACTID_MULTIM_TYPE))

            elif tType == TOKEN_NOP:
                self.v = NopCAction.INSTANCE

            elif tType == TOKEN_UNSET:
                self.v = UnsetCAction.INSTANCE

        else:
            self.type = PTYPE_STRING
            self.v = str(value)


    def getType(self):
        return self.type


    def isOfType(self, type):
        return self.type == type


    def __str__(self):
        return "%s, tp=%s" % (self.v, self.type)

    def __repr__(self):
        return self.__str__()




    @staticmethod
    def __makeInteger(val):
        vL = val.lower()

        vn = 0

        if vL == "0" or vL == "0b":
            vn = 0

        elif vL.startswith("0b"):
            vn = int(vL[2:], 2)

        elif vL.endswith("b"):
            vn = int(vL[:-1], 2)

        elif vL.startswith("0d") or vL.startswith("0i"):
            vn = int(vL[2:], 10)

        elif vL.endswith("d") or vL.endswith("i"):
            vn = int(vL[:-1], 10)

        elif vL.startswith("0h") or vL.startswith("0x"):
            vn = int(vL[2:], 16)

        elif vL.endswith("h") or vL.endswith("x"):
            vn = int(vL[:-1], 16)

        elif vL.startswith("0o"):
            vn = int(vL[2:], 8)

        elif vL.startswith("0"):
            vn = int(vL[1:], 8)

        elif vL.endswith("o"):
            vn = int(vL[:-1], 8)

        else:
            vn = int(vL, 10)

        return vn


    @staticmethod
    def __makeFloat(val):
        if val.find(".") != -1:
            v = val
        else:
            v = Value.__makeInteger(val)

        return float(v)



    @staticmethod
    def  __isTokenInteger(tType):
        return tType in (TOKEN_DECIMAL_INTEGER, TOKEN_BINARY_INTEGER, TOKEN_OCTAL_INTEGER, TOKEN_HEXADECIMAL_INTEGER,)

    @staticmethod
    def  __isTokenBoolean(tType):
        return tType in (TOKEN_TRUE, TOKEN_FALSE,)

    @staticmethod
    def __isTokenCustomAction(tType):
        return tType in (TOKEN_KEYS, TOKEN_MOUSE, TOKEN_FUNCT, TOKEN_EXEC, TOKEN_SYSOP, TOKEN_MULTIMEDIA, TOKEN_NOP, TOKEN_UNSET,)


    @staticmethod
    def __collectKeystrokes(elems):
        keystrkLs = []
        keystrkInst = None
        firstTime = True

        for currT in elems:
            currType = currT.getTokenType()

            if firstTime:
                keystrkInst = Keystroke()
                keystrkLs.append(keystrkInst)
                firstTime = False

            if currType in (TOKEN_IDENTIFIER, TOKEN_GARBAGE, TOKEN_TRUE, TOKEN_FALSE,):
                keystrkInst.addKey(SingleKey.fromKeyName(currT.getTokenValue()))

            elif currType == TOKEN_ARG_SEP:
                keystrkInst = Keystroke()
                keystrkLs.append(keystrkInst)

        return keystrkLs



    @staticmethod
    def __collectMouseKeys(elems):
        mKeys = []

        for tk in elems:
            actidInst = Value.__collectSingleActid(tk, ACTID_MOUSEK_VALUES, ACTID_MOUSEK_TYPE)
            mKeys.append(actidInst)

        return mKeys



    @staticmethod
    def __collectSingleActid(tok, validGroup, validType):
        currType = tok.getTokenType()

        singleActidInst = None

        if currType in (TOKEN_IDENTIFIER, TOKEN_GARBAGE, TOKEN_TRUE, TOKEN_FALSE,):
            singleActidInst = SingleActid.fromActid(tok.getTokenValue(), validGroup, validType)

        elif Value.__isTokenInteger(currType):
            singleActidInst = SingleActid.fromActid(Value.__makeInteger(tok.getTokenValue()), validGroup, validType)

        return singleActidInst