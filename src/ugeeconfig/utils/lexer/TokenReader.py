from abc import ABC, abstractmethod

from .TokenInfo import *



class TokenReader(ABC):
    def __init__(self, inpread):
        self.inpread = inpread

    @abstractmethod
    def isValidCharacter(self, ch):
        pass

    @abstractmethod
    def getTokenType(self):
        pass

    @abstractmethod
    def initForIteration(self):
        pass


    def tokenize(self):
        validInput = True
        while validInput:
            ch = self.inpread.next()
            if ch is None: # EOI reached
                validInput = False
            else:
                #print("chr: " + str(ch))
                validInput = self.isValidCharacter(ch)
                #print("is valid: " + str(validInput))
                if not validInput:
                    self.inpread.putback()
                    #print("length put back to: " + str(self.inpread.length))

        if self.inpread.getCurrentLength() == 0: # If there are no characters, it means that the check already failed, ergo, the tokenReader didn't found anything useful, use the next one
            return None # This TokenReader failed, try another one

        if self.getTokenType() == TOKEN_INVALID:
            self.inpread.putbackAll() # put back everything, so that the necessary can be analyzed by another TokenReader
            return None


        return TokenInfo(self.getTokenType(), self.inpread.extract())
