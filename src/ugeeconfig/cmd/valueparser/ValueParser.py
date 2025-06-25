from .ValueTokenizer import *
from .ValueExceptions import *

from ...data.Action import *
from ...utils.utils import str_equals_insensitive, printf
from ...utils.Stack import *


NT_S = "nt_s"
NT_A = "nt_a"
NT_B = "nt_b"
NT_C = "nt_c"

TG_NOARGF = "tg_noargf" # unset, nop
TG_SNARGF = "tg_snargf" # funct, sysop, multimedia
TG_INTEGER = "tg_integer"
TG_KEY = "tg_key" # Possible key that appear in keys() command (identifier, t and f)
TG_NUMERIC = "tg_numeric" # both float and integer
TG_ACTID = "tg_actid" # identifer and/or integer
TG_STRING = "tg_string" # identifier and garbage


DEBUG_PARSING = False


ER = -1

CELL_NOARGF = 0
CELL_SNARGF = 1
CELL_INTEGER = 2
CELL_IDENTIFIER = 3
CELL_FLOAT = 4
CELL_KEYS = 5
CELL_MOUSE = 6
CELL_EXEC = 7
CELL_GOPEN  = 8
CELL_SEP = 9
CELL_GCLOSE = 10
CELL_PLUS = 11
CELL_TRUE = 12
CELL_FALSE = 13
CELL_RECTANGLE = 14
CELL_PRESSURE = 15
CELL_GARBAGE = 16
CELL_EOI = 17


class ValueParser(object):
    PRODUCTIONS_TABLE = {
         0:  ( NT_S  ,  TG_NOARGF, NT_A, TOKEN_EOI, ),
         1:  ( NT_A  ,  TOKEN_ARG_GOPEN, TOKEN_ARG_GCLOSE, ),
         2:  ( NT_A  ,  ),
         3:  ( NT_S  ,  TG_SNARGF, TOKEN_ARG_GOPEN, TG_ACTID, TOKEN_ARG_GCLOSE, TOKEN_EOI, ),
         4:  ( NT_S  ,  TOKEN_EXEC, TOKEN_ARG_GOPEN, TG_STRING, TOKEN_ARG_GCLOSE, TOKEN_EOI, ),
         5:  ( NT_S  ,  TOKEN_MOUSE, TOKEN_ARG_GOPEN, TG_ACTID, NT_B, TOKEN_EOI, ),
         6:  ( NT_B  ,  TOKEN_ARG_PLUS, TG_ACTID, NT_B, ),
         7:  ( NT_B  ,  TOKEN_ARG_GCLOSE, ),

         8:  ( NT_S  ,  TOKEN_KEYS, TOKEN_ARG_GOPEN, TG_KEY, NT_C, TOKEN_EOI, ),
         9:  ( NT_C  ,  TOKEN_ARG_PLUS, TG_KEY, NT_C, ),
        10:  ( NT_C  ,  TOKEN_ARG_GCLOSE, ),
        11:  ( NT_S  ,  TOKEN_TRUE, TOKEN_EOI, ),
        12:  ( NT_S  ,  TOKEN_FALSE, TOKEN_EOI, ),
        13:  ( NT_S  ,  TG_INTEGER, TOKEN_EOI, ),
        14:  ( NT_S  ,  TOKEN_RECTANGLE, TOKEN_ARG_GOPEN, TG_INTEGER, TOKEN_ARG_SEP, TG_INTEGER, TOKEN_ARG_SEP, TG_INTEGER, TOKEN_ARG_SEP, TG_INTEGER, TOKEN_ARG_GCLOSE, TOKEN_EOI, ),
        15:  ( NT_S  ,  TOKEN_PRESSURE, TOKEN_ARG_GOPEN, TG_NUMERIC, TOKEN_ARG_SEP, TG_NUMERIC, TOKEN_ARG_SEP, TG_NUMERIC, TOKEN_ARG_SEP, TG_NUMERIC, TOKEN_ARG_GCLOSE, TOKEN_EOI, ),
        16:  ( NT_S  ,  TG_STRING, TOKEN_EOI, ),
        17:  ( NT_S  ,  ),
        18:  ( NT_C  ,  TOKEN_ARG_SEP, TG_KEY, NT_C, ),
        19:  ( NT_S  ,  TOKEN_FLOAT, TOKEN_EOI, ),
    }

    LL1_TABLE = {
        #        [NOARGF] [SNARGF] [INTEGER] IDENTIFIER FLOAT keys mouse exec   (   ,   )   +   T   F  RT  PR  GRB   $
        NT_S:   (       0,       3,      13,         16,   19,   8,    5,   4, ER, ER, ER, ER, 11, 12, 14, 15,  16, 17 ),
        NT_A:   (      ER,      ER,      ER,         ER,   ER,  ER,   ER,  ER,  1, ER, ER, ER, ER, ER, ER, ER,  ER,  2 ),
        NT_B:   (      ER,      ER,      ER,         ER,   ER,  ER,   ER,  ER, ER, ER,  7,  6, ER, ER, ER, ER,  ER, ER ),
        NT_C:   (      ER,      ER,      ER,         ER,   ER,  ER,   ER,  ER, ER, 18, 10,  9, ER, ER, ER, ER,  ER, ER ),
    }


    def __init__(self, inp):
        self.tokz = ValueTokenizer(inp)


    @staticmethod
    def __getTokenCell(tokenType):
        t = None

        if tokenType in (TOKEN_NOP, TOKEN_UNSET,):
            t = CELL_NOARGF

        elif tokenType in (TOKEN_FUNCT, TOKEN_EXEC, TOKEN_SYSOP, TOKEN_MULTIMEDIA,):
            t = CELL_SNARGF

        elif tokenType in (TOKEN_DECIMAL_INTEGER, TOKEN_BINARY_INTEGER, TOKEN_HEXADECIMAL_INTEGER,TOKEN_OCTAL_INTEGER,):
            t = CELL_INTEGER

        elif tokenType == TOKEN_IDENTIFIER:
            t = CELL_IDENTIFIER

        elif tokenType == TOKEN_FLOAT:
            t = CELL_FLOAT

        elif tokenType == TOKEN_KEYS:
            t = CELL_KEYS

        elif tokenType == TOKEN_MOUSE:
            t = CELL_MOUSE

        elif tokenType == TOKEN_EXEC:
            t = CELL_EXEC

        elif tokenType == TOKEN_ARG_GOPEN:
            t = CELL_GOPEN

        elif tokenType == TOKEN_ARG_SEP:
            t = CELL_SEP

        elif tokenType == TOKEN_ARG_GCLOSE:
            t = CELL_GCLOSE

        elif tokenType == TOKEN_ARG_PLUS:
            t = CELL_PLUS

        elif tokenType == TOKEN_TRUE:
            t = CELL_TRUE

        elif tokenType == TOKEN_FALSE:
            t = CELL_FALSE

        elif tokenType == TOKEN_RECTANGLE:
            t = CELL_RECTANGLE

        elif tokenType == TOKEN_PRESSURE:
            t = CELL_PRESSURE

        elif tokenType == TOKEN_GARBAGE:
            t = CELL_GARBAGE

        elif tokenType == TOKEN_EOI:
            t = CELL_EOI

        return t


    @staticmethod
    def getProdNo(nt, t):
        cell = ValueParser.__getTokenCell(t)
        if cell is None:
            return None

        prodNo = ValueParser.LL1_TABLE[nt][cell]
        return prodNo


    @staticmethod
    def isNT(t):
        return t in (NT_S, NT_A, NT_B, NT_C,)


    @staticmethod
    def isTokenGroup(t):
        return t in (TG_NOARGF, TG_SNARGF, TG_INTEGER, TG_NUMERIC, TG_ACTID, TG_STRING, TG_KEY)



    def parse(self):
        toks = []

        st = Stack()
        st.push(NT_S)

        captureToken = True

        while not st.isEmpty():
            currNT = st.pop()

            if captureToken:
                ValueParser.__printf("Capturing new token...")
                currT = self.tokz.nextToken()
                currType = currT.getTokenType()
                ValueParser.__printf(currT)
                while currType == TOKEN_SPACE:
                    currT = self.tokz.nextToken()
                    currType = currT.getTokenType()

                captureToken = False


            if ValueParser.isNT(currNT):
                ValueParser.__printf("At the top of the stack NT \"%s\" was found" % (currNT,))
                ValueParser.__printf("Current token: " + str(currT))
                prodNo = ValueParser.getProdNo(currNT, currType)
                if prodNo == ER:
                    raise ValueParserException("Syntax error: unexpected token \"%s\"" % (currType,))

                prod = ValueParser.PRODUCTIONS_TABLE[prodNo]
                prodNT = prod[0]
                prodEls = prod[1:]
                ValueParser.__printf("Chosen production %d (%s->%s)" % (prodNo, prodNT, prodEls,))
                if len(prodEls) == 0:
                    print("Empty production")

                for i in tuple(reversed(prodEls)):
                    if ValueParser.isTokenGroup(i):
                        ValueParser.__printf("Adding token group %s to stack" % (i,))
                    else:
                        ValueParser.__printf("Adding token %s to stack" % (i,))
                    st.push(i)

            elif ValueParser.isTokenGroup(currNT):
                ValueParser.__printf("At the top of the stack token group \"%s\" was found (pushing into it again)" % (currType,))
                if not ValueParser.isValidTokenForTokenGroup(currT, currNT):
                    raise ValueParserException("Syntax error: expected element valid for token group \"%s\" but \"%s\" was found!" % (currNT, currType,))

                st.push(currType)

            elif currNT == currType:
                ValueParser.__printf("At the top of the stack token \"%s\" was found" % (currType,))
                ValueParser.__printf("Top of the stack and current token concide... collecting token...")
                if not ValueParser.isTokenToIgnore(currType):
                    toks.append(currT)
                captureToken = True

            else:
                raise ValueParserException("Syntax error: expected token \"%s\" but \"%s\" was found!" % (currNT, currType,))

        return toks



    @staticmethod
    def isTokenToIgnore(tokType):
        return tokType in (TOKEN_SPACE, TOKEN_ARG_GOPEN, TOKEN_ARG_GCLOSE, TOKEN_ARG_PLUS, TOKEN_EOI,)


    @staticmethod
    def isValidTokenForTokenGroup(token, tokGroup):
        tokType = token.getTokenType()

        if tokGroup == TG_NOARGF:
            return tokType in (TOKEN_UNSET, TOKEN_NOP,)
        elif tokGroup == TG_SNARGF:
            return tokType in (TOKEN_FUNCT, TOKEN_SYSOP, TOKEN_MULTIMEDIA,)
        elif tokGroup == TG_INTEGER:
            return ValueParser.__isIntegerTokType(tokType)
        elif tokGroup == TG_NUMERIC:
            return ValueParser.__isIntegerTokType(tokType) or tokType == TOKEN_FLOAT
        elif tokGroup == TG_ACTID:
            return ValueParser.__isIntegerTokType(tokType) or tokType == TOKEN_IDENTIFIER
        elif tokGroup == TG_STRING:
            return tokType in (TOKEN_IDENTIFIER, TOKEN_GARBAGE,)
        elif tokGroup == TG_KEY:
            return tokType in (TOKEN_IDENTIFIER, TOKEN_TRUE, TOKEN_FALSE) or ValueParser.__isIntegerTokType(tokType)

    @staticmethod
    def __isIntegerTokType(tokType):
        return tokType in (TOKEN_DECIMAL_INTEGER, TOKEN_BINARY_INTEGER, TOKEN_OCTAL_INTEGER, TOKEN_HEXADECIMAL_INTEGER,)



    @staticmethod
    def __printf(message, newline=True):
        if DEBUG_PARSING:
            if not isinstance(message, str):
                message = str(message)
            printf(message)
            if newline:
                printf("\n")