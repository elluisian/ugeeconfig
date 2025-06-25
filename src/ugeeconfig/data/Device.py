# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from copy import deepcopy


from .App import *
from .AppId import *
from .Common import *



class Device(object):
    def __init__(self, name, deviceinfo, common, commonapp, apps):
        self.name = name
        self.deviceinfo = deviceinfo
        self.common = common
        self.commonapp = commonapp

        self.apps = []
        self.appsSz = 0
        for i in apps:
            self.apps.append(i)
            self.appsSz += 1


    @staticmethod
    def makeDevice(devname, devinfo, devpic, appsettings, sc, screenmapping, tabletpannel):
        return Device(
            name = devname,
            deviceinfo = devinfo,
            common = Common(
                screenmapping = screenmapping,
                tabletpannel = tabletpannel,
                picturefiles = devpic,
                sc = sc,
                enable_messages = True,
                enable_tabletkeys = True,
                enable_pressure = True,
                enable_slope = True
            ),
            commonapp = App(
                appid = None,
                appsettings = appsettings
            ),
            apps = (
                App(
                    appid = AppId(id = 0, name = 0),
                    appsettings = deepcopy(appsettings)
                ),
            )
        )


    def getCommon(self):
        return self.common


    def getCommonApp(self):
        return self.commonapp


    """
    This part is a WIP, as it tries to consider the possibility of adding "custom apps", while not supported on Linux...
    This part was not correctly studied, app with id = 0 and name = 0 is considered to be the default config and it is used to get the default settings for new apps.
    """
    def getApp(self, idx):
        if 1 <= idx < self.appsSz:
            return self.apps[idx]

        return None


    def addApp(self, appid, appname, apppath):
        app = App(
            AppId(appid, appname, apppath),
            deepcopy(self.apps[0].getSettings())
        )

        self.apps.append(app)
        self.appsSz += 1


    def removeApp(self, appInst):
        try:
            idx = self.apps.index(appInst)
            if idx == 0:
                return
            del self.apps[idx]
        except ValueError:
            pass