# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



TOKEN_EOI = "eoi"
TOKEN_INVALID = "invalid" # Used in order to let other TokenReaders analyze

TOKEN_IDENTIFIER = "identifier"

TOKEN_SPACE = "space"
TOKEN_GARBAGE = "garbage"
TOKEN_NUMERIC_GARBAGE = "numeric_garbage"
TOKEN_BINARY_INTEGER = "binint"
TOKEN_OCTAL_INTEGER = "octint"
TOKEN_DECIMAL_INTEGER = "decint"
TOKEN_HEXADECIMAL_INTEGER = "hexint"
TOKEN_FLOAT = "float"





class TokenInfo(object):
    def __init__(self, tp, value):
        self.tp = tp
        self.value = value


    @staticmethod
    def makeEOIToken():
        return TokenInfo(TOKEN_EOI, TOKEN_EOI)


    def __str__(self):
        return "%s: \"%s\"" % (self.tp, self.value)

    def __repr__(self):
        return self.__str__()

    def isEOI(self):
        return self.tp == TOKEN_EOI

    def isInvalid(self):
        return self.tp == TOKEN_INVALID

    def getTokenType(self):
        return self.tp

    def getTokenValue(self):
        return self.value

    def isTokenType(self, tokType):
        return self.tp == tokType

    def isTokenValue(self, tokValue):
        return self.value == tokValue