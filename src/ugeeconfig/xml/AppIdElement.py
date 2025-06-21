from ..utils.utils import *
from ..data.AppId import *


class AppIdElement(XMLElement):
    def writeToElement(self, data, parent=None):
        appid = data

        elem = XMLElement.handleTagWithParent("app", parent)

        elem.attrib["id"] = str(appid.id)
        elem.attrib["name"] = str(appid.name)
        elpt = etree.SubElement(elem, "path")
        if appid.path is not None:
            elpt.text = str(appid.path)

        return elem



    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        if elem.tag != "app":
            raise InvalidXMLTag("Element \"%s\" is invalid, \"app\" expected!" % (elem.tag,))

        idd = xmint_to_int(elem.attrib["id"])
        name = elem.attrib["name"]
        path = None

        children = get_children(elem)
        for child in children:
            if child.tag == "path":
                if child.text is not None:
                    path = child.text

        return AppId(idd, name, path)