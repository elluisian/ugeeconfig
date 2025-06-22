from copy import deepcopy
from ..utils.Object import *


class AppSettings(object):
    def __init__(self, pressurepoints, tablepc, relativecoords, penbtns=(), tabletbtns=(), rings=()):
        self.pressurepoints = pressurepoints
        self.tablepc = tablepc
        self.relativecoords = Object(relativecoords)
        self.penbtns = penbtns
        self.tabletbtns = tabletbtns
        self.rings = rings


    @staticmethod
    def defaultRelativeCoords():
        return {"enabled": False, "speed": 5}


    def getPenBtn(self, name):
        for i in self.penbtns:
            if i.tagNo == name:
                return i

        return None


    def getPenBtnNames(self):
        btns = []
        for i in self.penbtns:
            btns.append(i.tagNo)

        return btns



    def getTabletBtn(self, name):
        for i in self.tabletbtns:
            if i.tagNo == name:
                return i

        return None


    def getTabletBtnNames(self):
        btns = []
        for i in self.tabletbtns:
            btns.append(i.tagNo)

        return btns


    def getRings(self):
        return list(self.rings)


    def getRingNames(self):
        btns = []
        for i in self.rings:
            btns.append(i.tag_name)

        return btns


    def getRingByTagName(self, ringName):
        ring = None
        for i in self.rings:
            if i.tag_name == ringName:
                ring = i
                break

        return ring


    def __deepcopy__(self, m):
        return AppSettings(deepcopy(self.pressurepoints), self.tablepc, self.relativecoords.asDict(), tuple(map(lambda x : deepcopy(x), self.penbtns)), tuple(map(lambda x : deepcopy(x), self.tabletbtns)), tuple(map(lambda x : deepcopy(x), self.rings)))