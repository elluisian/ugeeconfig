# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



class Stack(object):
    def __init__(self):
        self.__data = []
        self.__dataSz = 0

    def push(self, datum):
        self.__data.append(datum)
        self.__dataSz += 1

    def top(self):
        if self.isEmpty():
            return None

        return self.__data[self.__dataSz - 1]

    def pop(self):
        t = self.top()
        if t is not None:
            del self.__data[self.__dataSz - 1]
            self.__dataSz -= 1
        return t

    def size(self):
        return self.__dataSz

    def isEmpty(self):
        return self.size() == 0

    def __deepcopy__(self, memo):
        stk = Stack()
        stk.__data = list(self.__data)
        stk.__dataSz = self.__dataSz
        return stk


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        msg = "STK<"

        for idx, datum in enumerate(self.__data):
            if datum is None:
                msg += "NONE"
            else:
                msg += str(datum)

            if idx < self.__dataSz - 1:
                msg += ","

        msg += ">"
        return msg


    def clear(self):
        self.__data.clear()
        self.__dataSz = 0