# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..utils.utils import *


class PressurePointsElement(XMLElement):
    def writeToElement(self, data, parent=None):
        pressurepoints = data

        elem = parent

        XMLElement.append_simple_element("P0", pressurepoints.p0, elem)
        XMLElement.append_simple_element("P1X", pressurepoints.p1.x, elem)
        XMLElement.append_simple_element("P1Y", pressurepoints.p1.y, elem)
        XMLElement.append_simple_element("P2", pressurepoints.p2, elem)

        return elem

    def readFromElement(self, elem=None, version=None):
        pass