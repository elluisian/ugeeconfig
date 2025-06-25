# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



class Object(object):
    def __init__(self, ds={}):
        self.__attrs = list(ds.keys())
        self.__values = {}
        for i in self.__attrs:
            v = ds[i]
            self.__values[i] = v
            setattr(self, i, v)


    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return self.__str__()

    def asDict(self):
        return dict(self.__values)