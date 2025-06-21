from abc import ABC, abstractmethod

from .InputReader import *
from .TokenInfo import *
from .CommonTokenReaders import GarbageTokReader


class Tokenizer(ABC):
    def __init__(self, inp, disruptingAlphabet):
        self.inpread = InputReader(inp)
        self.tokenReaders = list(self.getTokenReaders(self.inpread, disruptingAlphabet))
        self.tokenReaders.append(GarbageTokReader(self.inpread, disruptingAlphabet))


    @abstractmethod
    def getTokenReaders(self, inpr, disruptingAlphabet):
        pass



    def nextToken(self):
        if self.inpread.isEndOfInput():
            return TokenInfo.makeEOIToken()

        for tokread in self.tokenReaders:
            #print(tokread)
            tokread.initForIteration()
            el = tokread.tokenize()
            #Print("found: " + str(el))
            if el is not None:
                return el

        if self.inpread.getCurrentLength() > 0:
             # Passing this point, means that no token readers were able to detect what's going on, and there are still characters
            return None #TokenInfo(TOKEN_GARBAGE, self.inpread.extract())

        return None
