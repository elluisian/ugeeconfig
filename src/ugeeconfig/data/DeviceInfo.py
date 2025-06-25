# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



class DeviceInfo(object):
    def __init__(self, ringnum, keynum, pentype, trackpad=None, control=None, key_direction=None):
        self.ringnum = ringnum
        self.keynum = keynum
        self.pentype = pentype
        self.trackpad = trackpad
        self.control = control
        self.key_direction = key_direction