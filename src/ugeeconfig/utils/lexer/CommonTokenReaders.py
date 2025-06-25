# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from .TokenReader import *




class OperatorTokReader(TokenReader):
    def __init__(self, inpread, operator, tokenType):
        super().__init__(inpread)
        self.operator = operator
        self.tokenType = tokenType

    def initForIteration(self):
        pass

    def getTokenType(self):
        return self.tokenType

    def isValidCharacter(self, ch):
        return self.inpread.mayBeEqualTo(self.operator)

    @staticmethod
    def make(inpread, operator, tokenType):
        return OperatorTokReader(inpread, operator, tokenType)




class IdentifierKeywordTokReader(TokenReader):
    def __init__(self, inpread, disruptingAlphabet, tkDescrs=()):
        super().__init__(inpread)

        """
        The disrupting alphabet is the list of characters that will cause the Identifier TokenReader to stop itself when analyzing identifiers, since they take a broader form, compared to operators for example.
        """
        self.disruptingAlphabet = disruptingAlphabet

        self.keywords = []
        self.keywTypes = []
        self.insensitiveness = []

        for i in tkDescrs:
            keyword, keytype, insensitive = i
            self.keywords.append(keyword)
            self.keywTypes.append(keytype)
            self.insensitiveness.append(insensitive)

    def initForIteration(self):
        pass

    def getTokenType(self):
        for idx, keyw in enumerate(self.keywords):
            keywt = self.keywTypes[idx]
            insens = self.insensitiveness[idx]

            if (not insens and self.inpread.isEqualTo(keyw)) or\
                (insens and self.inpread.isEqualIgnoreCaseTo(keyw)):
                return keywt

        return TOKEN_IDENTIFIER


    def isValidCharacter(self, ch):
        l = self.inpread.getCurrentLength()
        if l == 1: # The first to be extracted
            return ch.isalpha() or ch == "_"

        if ch in self.disruptingAlphabet:
            return False

        return ch.isalpha() or ch.isnumeric() or self.__isAcceptedSymbol(ch)


    def __isAcceptedSymbol(self, ch):
        chVal = ord(ch)
        intervals = (
            range(33, 43), ## ! " # $ % & ' ( ) * +
            range(45, 47), ## - . /
            range(58, 64), ## : ; < = > ? @
            range(91, 96), ## [ \ ] ^ _ `
            range(123, 126) ## { | } ~
        )

        for i in intervals:
            if chVal in i:
                return True

        return False


    @staticmethod
    def make(inpread, disruptingAlphabet, *keywords):
        return IdentifierKeywordTokReader(inpread, disruptingAlphabet, keywords)




class SpaceTokReader(TokenReader):
    def __init__(self, inpr):
        super().__init__(inpr)

    def initForIteration(self):
        pass

    def isValidCharacter(self, ch):
        return ch.isspace()

    def getTokenType(self):
        return TOKEN_SPACE




class FloatTokReader(TokenReader):
    def __init__(self, inpr):
        super().__init__(inpr)
        self.initForIteration()

    def initForIteration(self):
        self.commaFound = False

    def isValidCharacter(self, ch):
        v = False

        if ch == ".":
            if self.commaFound:
                v = False
            else:
                self.commaFound = True
                v = True
        elif ch.isnumeric():
            v = True

        return v

    def getTokenType(self):
        return TOKEN_FLOAT if self.commaFound else TOKEN_INVALID




class GarbageTokReader(TokenReader):
    def __init__(self, inpr, disruptingAlphabet):
        super().__init__(inpr)
        self.disruptingAlphabet = disruptingAlphabet

    def initForIteration(self):
        pass

    def isValidCharacter(self, ch):
        return ch not in self.disruptingAlphabet

    def getTokenType(self):
        return TOKEN_GARBAGE
