# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.


from copy import deepcopy


class Ring(object):
    def __init__(self, tag_name, selected_wheel, mode=None, wheel_actmovements=[]):
        self.tag_name = tag_name
        self.selected_wheel = selected_wheel
        self.mode = mode
        self.wheel_actmovements = wheel_actmovements



    def getWheelActMovements(self):
        return list(self.wheel_actmovements)


    def getWheelActMovementByTagNo(self, tagno):
        for i in self.wheel_actmovements:
            if tagno == i.tagNo:
                return i
        return None


    def getWheelActMovementNames(self):
        whmov = []
        for i in self.wheel_actmovements:
            whmov.append(i.tagNo)

        return whmov


    def setSelectedWheel(self, selected_wheel):
        self.selected_wheel = selected_wheel


    def getSelectedWheel(self):
        return self.selected_wheel


    def __deepcopy__(self, m):
        return Ring(self.tag_name, self.selected_wheel, self.mode, list(map(lambda x : deepcopy(x), self.getWheelActMovements())))