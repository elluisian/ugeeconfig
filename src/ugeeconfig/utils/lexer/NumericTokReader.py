from .TokenReader import *


TOKEN_BINARY_INTEGER = "binint"
TOKEN_OCTAL_INTEGER = "octint"
TOKEN_DECIMAL_INTEGER = "decint"
TOKEN_HEXADECIMAL_INTEGER = "hexint"



# 0-PREFIXED (C-like)
#   01234  OCT
#  0o1236 OCT
# 0b01010 BIN
#  0x123A HEX
# 0d12340 DEC

# 12340451239 (Standard integer value)

# letter-SUFFIXED (assembly-like)
#   123o OCTAL
#  1234d DECIMAL
#   123h HEX
# 01010b BIN



STATE_START = 0
"""
STATE_ZERO_PREFIXED = 1
STATE_BINONLY_DECIMAL = 17
STATE_BINARY_SUFFIXED = 20
STATE_HEXADECIMAL = 12
STATE_OCTAL_ZERO_PREFIXED =  10
STATE_OCTAL_SUFFIXED = 14
STATE_DECONLY_DECIMAL = 11
STATE_DECIMAL_ISUFFIXED = 16
STATE_DECIMAL_DSUFFIXED = 15
STATE_HEXADECIMAL_SUFFIXED = 13
STATE_BINARY_PREFIXED = 6
STATE_OCTAL_PREFIXED = 7
STATE_DECIMAL_PREFIXED = 8
STATE_HEXADECIMAL_PREFIXED = 9
STATE_BINARY_PREFIX = 2
STATE_OCTAL_PREFIX = 3
STATE_DECIMAL_IPREFIX = 4
STATE_DECIMAL_DPREFIX = 22
STATE_HEXADECIMAL_PREFIX = 5
STATE_OCTONLY_DECIMAL = 21
"""

PT = -4

class NumericTokReader(TokenReader):
    DFA = {
      #        0   1   2   3   4   5   6   7   8   9   A   B   C   D   E   F   O   I  HX
         0: (  1, 17, 21, 21, 21, 21, 21, 21, 11, 11, PT, PT, PT, PT, PT, PT, PT, PT, PT, ),
         1: ( 17, 17, 10, 10, 10, 10, 10, 10, 10, 10, 12,  2, 12, 22, 12, 12,  3,  4,  5, ),
         2: (  6,  6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, PT, PT, 13, ),
         3: (  7,  7,  7,  7,  7,  7,  7,  7, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, ),
         4: (  8,  8,  8,  8,  8,  8,  8,  8,  8,  8, PT, PT, PT, PT, PT, PT, PT, PT, PT, ),
         5: (  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9, PT, PT, PT, ),
         6: (  6,  6, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, ),
         7: (  7,  7,  7,  7,  7,  7,  7,  7, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, PT, ),
         8: (  8,  8,  8,  8,  8,  8,  8,  8,  8,  8, PT, PT, PT, PT, PT, PT, PT, PT, PT, ),
         9: (  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9, PT, PT, PT, ),
        10: ( 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 12, 12, 12, 15, 12, 12, 14, 16, 13, ),
        11: ( 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 15, 12, 12, 12, 12, PT, 16, 13, ),
        12: ( 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, PT, PT, 13, ),
        13: (),
        14: (),
        15: (),
        16: (),
        17: ( 17, 17, 21, 21, 21, 21, 21, 21, 11, 11, 12, 20, 12, 12, 12, 12, 14, 16, 13, ),
        20: ( 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, PT, PT, 13, ),
        21: ( 21, 21, 21, 21, 21, 21, 21, 21, 11, 11, 12, 12, 12, 12, 12, 12, 14, 16, 13, ),
        22: (  8,  8,  8,  8,  8,  8,  8,  8,  8,  8, PT, 12, 12, 12, 12, 12, PT, PT, 13, ),
    }


    DFA_TOKEN = {
         0: TOKEN_NUMERIC_GARBAGE,
         1: TOKEN_DECIMAL_INTEGER,
         2: TOKEN_BINARY_INTEGER,
         3: TOKEN_OCTAL_INTEGER,
         4: TOKEN_DECIMAL_INTEGER,
         5: TOKEN_HEXADECIMAL_INTEGER,
         6: TOKEN_BINARY_INTEGER,
         7: TOKEN_OCTAL_INTEGER,
         8: TOKEN_DECIMAL_INTEGER,
         9: TOKEN_HEXADECIMAL_INTEGER,
        10: TOKEN_OCTAL_INTEGER,
        11: TOKEN_DECIMAL_INTEGER,
        12: TOKEN_NUMERIC_GARBAGE,
        13: TOKEN_HEXADECIMAL_INTEGER,
        14: TOKEN_OCTAL_INTEGER,
        15: TOKEN_DECIMAL_INTEGER,
        16: TOKEN_DECIMAL_INTEGER,
        17: TOKEN_DECIMAL_INTEGER,
        20: TOKEN_BINARY_INTEGER,
        21: TOKEN_DECIMAL_INTEGER,
        22: TOKEN_DECIMAL_INTEGER,
    }


    def __init__(self, inpread):
        super().__init__(inpread)



    def initForIteration(self):
        self.state = STATE_START
        self.prevState = self.state


    @staticmethod
    def getCell(ch):
        dd = None

        if NumericTokReader.isDecimalDigit(ch):
            dd = ord(ch) - ord("0")

        elif NumericTokReader.isHexadecimalTransitionalDigit(ch):
            dd = (ord(ch.upper()) - ord("A")) + 10

        elif NumericTokReader.isOctalPrefix(ch):
            dd = 16

        elif NumericTokReader.isDecimalIPrefix(ch):
            dd = 17

        elif NumericTokReader.isHexadecimalPrefix(ch):
            dd = 18

        return dd



    def isValidCharacter(self, ch):
        #print("I AM AT: " + str(self.state) + " with ch: " + ch)

        cell = NumericTokReader.getCell(ch)
        if cell is None:
            return False

        if self.state == PT:
            return False

        stdata = NumericTokReader.DFA[self.state]
        if len(stdata) == 0:
            return False

        # Save the last valid state before going on
        self.prevState = self.state
        self.state = stdata[cell]

        return self.prevState != PT



    def getTokenType(self):
        if self.state == PT:
            return TOKEN_NUMERIC_GARBAGE

        return NumericTokReader.DFA_TOKEN[self.state]




    @staticmethod
    def isDecimalDigit(ch):
        return "0" <= ch <= "9"

    # That is, the digits that are used to transition to hexadecimal (from binary/octal/decimal)
    @staticmethod
    def isHexadecimalTransitionalDigit(ch):
        return "A" <= ch <= "F" or\
            "a" <= ch <= "f"

    @staticmethod
    def isOctalPrefix(ch):
        return ch in ("o", "O",)

    @staticmethod
    def isDecimalIPrefix(ch):
        return ch in ("i", "I",)

    @staticmethod
    def isHexadecimalPrefix(ch):
        return ch in ("h", "H", "x", "X",)