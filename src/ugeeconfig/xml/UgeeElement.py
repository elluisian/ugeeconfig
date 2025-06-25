# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..data.Ugee import *

from .DesktopShortcutKeysElement import *
from .DeviceElement import *



PENTABLET_LISTS_VERSION = "1.4.1"


class UgeeElement(XMLElement):
    def writeToElement(self, data, parent=None):
        ugee = data.ugee
        pentbversion = data.pentbversion

        root = etree.Element("UGEE")

        if ugee.pentables is not None:
            elem = etree.SubElement(root, "PenTableLists")
            elem.attrib["version"] = pentbversion

            for i in ugee.pentableNames:
                devinst = ugee.pentables[i]
                devel = DeviceElement()
                devel.writeToElement(devinst, elem)

        if ugee.desktopskeys is not None:
            deskscutel = DesktopShortcutKeysElement()
            deskscutel.writeToElement(ugee.desktopskeys, root)

        return root



    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element \"None\" passed")

        if elem.tag != "UGEE":
            raise InvalidXMLTag("Element \"%s\" is invalid, \"UGEE\" expected!" % (elem.tag,))

        pentables = {}
        desktopskeys = None

        children = get_children(elem)
        for child in children:
            if child.tag == "PenTableLists":
                devs = get_children(child)
                version = child.attrib["version"]
                for dev in devs:
                    ddel = DeviceElement()
                    devinst = ddel.readFromElement(dev, version)
                    pentables[devinst.name] = devinst

            elif child.tag == "DesktopShortcutKeys":
                dskel = DesktopShortcutKeysElement()
                desktopskeys = dskel.readFromElement(child, version)

            else:
                raise InvalidXMLTag("Element \"%s\" is invalid during the analysis of \"UGEE\"" % (child.tag,))


        return Ugee(pentables, desktopskeys)