# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



class Common(object):
    def __init__(self, screenmapping, tabletpannel, picturefiles, sc, enable_messages, enable_tabletkeys, enable_pressure, enable_slope):
        self.screenmapping = screenmapping
        self.tabletpannel = tabletpannel
        self.picturefiles = picturefiles
        self.sc = sc

        self.enable_messages = enable_messages
        self.enable_tabletkeys = enable_tabletkeys
        self.enable_pressure = enable_pressure
        self.enable_slope = enable_slope