from ..utils.utils import *
from ..data.SC import *


class SCElement(XMLElement):
    def writeToElement(self, data, parent=None):
        sc = data

        elem = XMLElement.handleTagWithParent("SC", parent)

        elem.attrib["fKX"] = int_to_xmint(sc.fKX)
        elem.attrib["fYLC"] = int_to_xmint(sc.fYLC)
        elem.attrib["fXLC"] = int_to_xmint(sc.fXLC)
        elem.attrib["fKY"] = int_to_xmint(sc.fKY)

        return elem


    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        if elem.tag != "SC":
            raise InvalidXMLTag("Element \"%s\" is invalid, \"SC\" expected!" % (elem.tag,))


        fKX = xmint_to_int(elem.attrib["fKX"])
        fYLC = xmint_to_int(elem.attrib["fYLC"])
        fXLC = xmint_to_int(elem.attrib["fXLC"])
        fKY = xmint_to_int(elem.attrib["fKY"])

        return SC(fKX, fYLC, fXLC, fKY)