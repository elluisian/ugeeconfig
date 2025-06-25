# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..data.App import *
from ..utils.utils import *
from .AppIdElement import *
from .AppSettingsElement import *


class AppElement(XMLElement):
    def writeToElement(self, data, parent=None):
        app = data

        isNonCommon = app.appid is not None
        if isNonCommon:
            appidel = AppIdElement()
            elem = appidel.writeToElement(app.appid, parent)
        else:
            if parent is None:
                elem = etree.Element("CommonAPP")
            else:
                elem = etree.SubElement(parent, "CommonAPP")

        appsettingsel = AppSettingsElement(not isNonCommon)
        appsettingsel.writeToElement(app.appsettings, elem)

        return elem



    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")


        isNonCommon = elem.tag != "CommonAPP"

        if isNonCommon:
            appidel = AppIdElement()
            appid = appidel.readFromElement(elem, version)

        else:
            appid = None

        appsettingsel = AppSettingsElement(not isNonCommon)
        appsett = appsettingsel.readFromElement(elem, version)

        return App(appid, appsett)