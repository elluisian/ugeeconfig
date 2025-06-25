from ..utils.Point import *

class PressurePoints(object):
    def __init__(self, p0, p1, p2):
        # These represent the points of pressure
        # P0 = first point with y = 1
        # P2 = second point with y = 0
        # P1 = middle point, with x = ?, y = ?

        self.p0 = p0
        self.p1 = p1
        self.p2 = p2


    @staticmethod
    def fromValues(p0, p1x, p1y, p2):
        # It must be so that:
        #
        # p0 <= p1.x <= p2
        # 0 <= p0 <= 1
        # 0 <= p2 <= 1
        # 0 <= p1.y <= 1

        if p0 <= p1x <= p2 and\
            0 <= p0 <= 1 and\
            0 <= p2 <= 1 and\
            0 <= p1y <= 1:
            return PressurePoints(p0, Point(p1x, p1y), p2)

        return PressurePoints.default()


    @staticmethod
    def default():
        return PressurePoints.fromValues(0, 0.5, 0.5, 1)


    def __str__(self):
        return "press(%.1f, %.1f:%.1f, %.1f)" % (self.p0, self.p1.x, self.p1.y, self.p2)

    def __repr__(self):
        return self.__str__()


    def __deepcopy__(self, m):
        return PressurePoints(self.p0, Point(self.p1.x, self.p1.y), self.p2)