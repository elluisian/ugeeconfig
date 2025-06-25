# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from .Point import *

class Rectangle(Point):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def __deepcopy__(self, m):
        return Rectangle(self.x, self.y, self.w, self.h)