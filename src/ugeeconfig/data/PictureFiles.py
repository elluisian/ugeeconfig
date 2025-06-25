# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..utils.Rectangle import *

class PictureFiles(object):
    def __init__(self, t0, t1, t2, t3):
        self.t0 = Rectangle(t0[0], t0[1], t0[2], t0[3])
        self.t1 = Rectangle(t1[0], t1[1], t1[2], t1[3])
        self.t2 = Rectangle(t2[0], t2[1], t2[2], t2[3])
        self.t3 = Rectangle(t3[0], t3[1], t3[2], t3[3])