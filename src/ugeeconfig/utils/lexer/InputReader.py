from ..utils import str_equals_insensitive


class InputReader(object):
    def __init__(self, inp):
        self.inp = inp
        self.inpSize = len(inp)
        # 0 to inpSize - 1

        #print(inp)

        self.latest_saved_idx = 0 # Latest idx where a token was saved (extracted), just before analyzing the current one
        self.length = 0



    def next(self):
        if self.isEndOfInput():
            return None

        ch = self.inp[self.latest_saved_idx + self.length]
        self.length += 1

        return ch



    def putback(self, n=1):
        if self.length - n > 0:
            self.length -= n
        else:
            self.length = 0



    def putbackAll(self, n=1):
        self.putback(self.length)



    def isEndOfInput(self):
        return self.latest_saved_idx + self.length >= self.inpSize


    def getCurrentLength(self):
        return self.length


    def getCurrentInput(self):
        return self.inp[self.latest_saved_idx:self.latest_saved_idx + self.length]


    def extract(self):
        buff = self.getCurrentInput()
        #print(buff)
        #print(self.length)
        self.latest_saved_idx += self.length
        self.length = 0
        #print(self.length)
        return buff


    def mayBeEqualTo(self, content):
        mayBe = True

        if self.length > len(content):
            return False

        #print(content)
        #print(self.length)

        for i in range(0, self.length):
            ch = self.inp[self.latest_saved_idx + i]
            #print(ch)
            if ch != content[i]:
                mayBe = False
                break

        return mayBe



    def isEqualTo(self, content):
        if self.length != len(content):
            return False

        #print(content)
        #print(self.length)

        for i in range(0, self.length):
            ch = self.inp[self.latest_saved_idx + i]
            #print(ch)
            if ch != content[i]:
                return False

        return True



    def isEqualIgnoreCaseTo(self, content):
        if self.length != len(content):
            return False

        for i in range(0, self.length):
            ch = self.inp[self.latest_saved_idx + i]
            if not str_equals_insensitive(ch, content[i]):
                return False

        return True