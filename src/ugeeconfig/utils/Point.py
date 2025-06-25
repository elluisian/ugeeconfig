# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __deepcopy__(self, m):
        return Point(self.x, self.y)