# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from ..utils.utils import *
from ..data.PictureFiles import *



class PictureFilesElement(XMLElement):
    def writeToElement(self, data, parent=None):
        picturefiles = data

        elem = XMLElement.handleTagWithParent("PictureFiles", parent)

        t = picturefiles.t0
        XMLElement.append_simple_element("T_0", None, elem, (("X", t.x), ("Y", t.y), ("W", t.w), ("H", t.h)))
        t = picturefiles.t1
        XMLElement.append_simple_element("T_1", None, elem, (("X", t.x), ("Y", t.y), ("W", t.w), ("H", t.h)))
        t = picturefiles.t2
        XMLElement.append_simple_element("T_2", None, elem, (("X", t.x), ("Y", t.y), ("W", t.w), ("H", t.h)))
        t = picturefiles.t3
        XMLElement.append_simple_element("T_3", None, elem, (("X", t.x), ("Y", t.y), ("W", t.w), ("H", t.h)))

        return elem


    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        if elem.tag != "PictureFiles":
            raise InvalidXMLTag("Element \"%s\" is invalid, \"PictureFiles\" expected!" % (elem.tag,))

        t0 = None
        t1 = None
        t2 = None
        t3 = None

        children = get_children(elem)
        for child in children:
            if child.tag.startswith("T_"):
                x = xmint_to_int(child.attrib["X"])
                y = xmint_to_int(child.attrib["Y"])
                w = xmint_to_int(child.attrib["W"])
                h = xmint_to_int(child.attrib["H"])

                if child.tag == "T_0":
                    t0 = (x, y, w, h)
                elif child.tag == "T_1":
                    t1 = (x, y, w, h)
                elif child.tag == "T_2":
                    t2 = (x, y, w, h)
                elif child.tag == "T_3":
                    t3 = (x, y, w, h)
                else:
                    raise InvalidXMLTag("Element \"%s\" is invalid during the analysis of \"PictureFiles\"!" % (child.tag,))

            else:
                raise InvalidXMLTag("Element \"%s\" is invalid during the analysis of \"PictureFiles\"!" % (child.tag,))

        return PictureFiles(t0, t1, t2, t3)