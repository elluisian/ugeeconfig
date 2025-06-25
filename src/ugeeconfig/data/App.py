# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



class App(object):
    def __init__(self, appid, appsettings):
        self.appid = appid
        self.appsettings = appsettings


    def getAppId(self):
        return self.appid

    def getSettings(self):
        return self.appsettings