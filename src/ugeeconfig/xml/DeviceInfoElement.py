# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..utils.utils import *
from ..data.DeviceInfo import *


class DeviceInfoElement(XMLElement):
    def writeToElement(self, data, parent=None):
        deviceinfo = data

        elem = XMLElement.handleTagWithParent("DeviceInfo", parent)

        XMLElement.append_simple_element("DeviceRingNum", int_to_xmint(deviceinfo.ringnum), elem)
        XMLElement.append_simple_element("DeviceKeyNum", int_to_xmint(deviceinfo.keynum), elem)
        XMLElement.append_simple_element("DevicePenType", int_to_xmint(deviceinfo.pentype), elem)
        if deviceinfo.trackpad is not None:
            XMLElement.append_simple_element("DeviceTrackPad", int_to_xmint(deviceinfo.trackpad), elem)
        if deviceinfo.control is not None:
            XMLElement.append_simple_element("DeviceControl", int_to_xmint(deviceinfo.control), elem)
        if deviceinfo.key_direction is not None:
            XMLElement.append_simple_element("DeviceKeyDirection", int_to_xmint(deviceinfo.key_direction), elem)

        return elem


    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        if elem.tag != "DeviceInfo":
            raise InvalidXMLTag("Element \"%s\" is invalid, \"DeviceInfo\" expected!" % (elem.tag,))

        ringnum = None
        keynum = None
        pentype = None
        trackpad = None
        control = None
        key_direction = None


        children = get_children(elem)

        for child in children:
            if child.tag == "DeviceRingNum":
                ringnum = xmint_to_int(child.text)

            elif child.tag == "DeviceKeyNum":
                keynum = xmint_to_int(child.text)

            elif child.tag == "DevicePenType":
                pentype = xmint_to_int(child.text)

            elif child.tag == "DeviceTrackPad":
                trackpad = xmint_to_int(child.text)

            elif child.tag == "DeviceControl":
                control = xmint_to_int(child.text)

            elif child.tag == "DeviceKeyDirection":
                key_direction = xmint_to_int(child.text)

            else:
                raise InvalidXMLTag("Element \"%s\" is invalid during the analysis of \"DeviceInfo\"" % (child.tag,))


        return DeviceInfo(ringnum, keynum, pentype, trackpad, control, key_direction)