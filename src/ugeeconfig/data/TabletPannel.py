# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..utils.Rectangle import *


class TabletPannel(Rectangle):
    def __init__(self, x, y, w, h, orientation):
        super().__init__(x, y, w, h)
        self.orientation = orientation # 0, 90, 180, 270



    def assignFromRectangle(self, rectInst):
        self.x = rectInst.x
        self.y = rectInst.y
        self.w = rectInst.w
        self.h = rectInst.h


    def __str__(self):
        return "%dx%d+%d+%d" % (self.w, self.h, self.x, self.y,)
        #return "%dx%d+%d+%d,rot=%d" % (self.w, self.h, self.x, self.y, self.orientation,)


    @staticmethod
    def default():
        return TabletPannel(x = 0, y = 0, w = 0, h = 0, orientation = 0)