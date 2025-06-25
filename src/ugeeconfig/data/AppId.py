# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



class AppId(object):
    def __init__(self, id, name, path=None):
        self.id = id
        self.name = name
        self.path = path

    def getId(self):
        return self.id

    def setId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPath(self):
        return self.path

    def setPath(self, path):
        self.path = path

    def __str__(self):
        return "%d: %s %s" % (self.id, self.name, self.path)