# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..utils.utils import *
from ..data.ScreenMapping import *


class ScreenMappingElement(XMLElement):
    def writeToElement(self, data, parent=None):
        screenmapping = data

        elem = XMLElement.handleTagWithParent("ScreenMapping", parent)

        elem.attrib["id"] = str(screenmapping.selected_option) # The menubar choice is reported as id
        XMLElement.append_simple_element("SX", screenmapping.x, elem)
        XMLElement.append_simple_element("SY", screenmapping.y, elem)
        XMLElement.append_simple_element("SW", screenmapping.w, elem)
        XMLElement.append_simple_element("SH", screenmapping.h, elem)

        return elem


    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        if elem.tag != "ScreenMapping":
            raise InvalidXMLTag("Element \"%s\" is invalid, \"ScreenMapping\" expected!" % (elem.tag,))

        children = get_children(elem)
        sx = 0
        sy = 0
        sw = 0
        sh = 0
        selected_opt = xmint_to_int(elem.attrib["id"])

        for child in children:
            if child.tag == "SX":
                sx = xmint_to_int(child.text)
            elif child.tag == "SY":
                sy = xmint_to_int(child.text)
            elif child.tag == "SW":
                sw = xmint_to_int(child.text)
            elif child.tag == "SH":
                sh = xmint_to_int(child.text)

        return ScreenMapping(sx, sy, sw, sh, selected_opt)