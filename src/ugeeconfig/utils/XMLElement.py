# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from abc import ABC, abstractmethod
from lxml import etree



class XMLElement(ABC):
    @abstractmethod
    def writeToElement(self, data, parent=None):
        pass

    @abstractmethod
    def readFromElement(self, elem, version=None):
        pass



    @staticmethod
    def handleTagWithParent(tag, parent=None):
        elem = etree.Element(tag)
        if parent is not None:
            parent.append(elem)
            #elem = etree.SubElement(parent, "tagname")
        return elem


    @staticmethod
    def asXML(elem):
        return "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n".encode("utf-8") + etree.tostring(elem, pretty_print=True)


    @staticmethod
    def writeXML(element, path):
        f = open(path, "wb")
        f.write(XMLElement.asXML(element))
        f.close()


    @staticmethod
    def readXML(path):
        f = open(path, "rb")
        content = f.read()
        f.close()
        return etree.fromstring(content)


    @staticmethod
    def append_simple_element(tagname, value, parent=None, attribs=None):
        if parent is None:
            el = etree.Element(tagname)
        else:
            el = etree.SubElement(parent, tagname)

        if value is not None:
            el.text = str(value)

        if attribs is not None:
            for key, value in attribs:
                el.attrib[key] = str(value)

        return el
