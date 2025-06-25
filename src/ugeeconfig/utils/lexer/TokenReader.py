from abc import ABC, abstractmethod

from .TokenInfo import *


"""
This is a token reader, that is, a special detector for a single Token type.
Some of the common tokens are given as TokenReaders in CommonTokenReaders.py
"""
class TokenReader(ABC):
    def __init__(self, inpread):
        self.inpread = inpread


    """
    This method is the one that describes HOW the current token is recognized according ALSO to the current character (ch).
    For the most part, this is the most difficult method to implement.
    It must return true if the current character is valid for that input, false otherwise.
    """
    @abstractmethod
    def isValidCharacter(self, ch):
        pass


    """
    This method is used to return a tokenType, that will be used to make the final token.
    """
    @abstractmethod
    def getTokenType(self):
        pass

    """
    This method is used when initializing variables that may become useful when implementing
    "isValidCharacter".
    """
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
