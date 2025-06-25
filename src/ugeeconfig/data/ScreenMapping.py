# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..utils.Rectangle import *

class ScreenMapping(Rectangle):
    def __init__(self, x, y, w, h, selected_res_opt):
        super().__init__(x, y, w, h)
        self.selected_option = selected_res_opt # Menubar choice


    @staticmethod
    def default():
        return ScreenMapping(x = 0, y = 0, w = 0, h = 0, selected_res_opt = 0)


    def assignFromRectangle(self, rectInst):
        self.x = rectInst.x
        self.y = rectInst.y
        self.w = rectInst.w
        self.h = rectInst.h


    def __str__(self):
        return "%dx%d+%d+%d" % (self.w, self.h, self.x, self.y,)
        #return "%dx%d+%d+%d,sel=%d" % (self.w, self.h, self.x, self.y, self.selected_option,)