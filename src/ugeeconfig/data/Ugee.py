# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..utils.utils import str_equals_insensitive


class Ugee(object):
    def __init__(self, pentables, desktopskeys):
        self.pentables = pentables
        self.pentableNames = tuple(self.pentables.keys())
        self.desktopskeys = desktopskeys


    def getPentable(self, pentableId):
        for i in self.pentableNames:
            if str_equals_insensitive(pentableId, i):
                return self.pentables[pentableId]

        return None


    def exists(self, device):
        return device in self.pentables


    def getAvailableDevices(self):
        return tuple(self.pentableNames)


    def getDesktopShortcutKeys(self):
        return self.desktopskeys