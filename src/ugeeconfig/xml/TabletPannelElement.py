from ..utils.utils import *
from ..data.TabletPannel import *


class TabletPannelElement(XMLElement):
    def writeToElement(self, data, parent=None):
        tabletpannel = data

        elem = XMLElement.handleTagWithParent("TabletPannel", parent)

        elem.attrib["Orientation"] = int_to_xmint(TabletPannelElement.degree_to_id(tabletpannel.orientation))
        XMLElement.append_simple_element("TX", tabletpannel.x, elem)
        XMLElement.append_simple_element("TY", tabletpannel.y, elem)
        XMLElement.append_simple_element("TW", tabletpannel.w, elem)
        XMLElement.append_simple_element("TH", tabletpannel.h, elem)

        return elem



    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        if elem.tag != "TabletPannel":
            raise InvalidXMLTag("Element \"%s\" is invalid, \"TabletPannel\" expected!" % (elem.tag,))

        children = get_children(elem)
        tx = 0
        ty = 0
        tw = 0
        th = 0
        selected_orientation = TabletPannelElement.id_to_degree(xmint_to_int(elem.attrib["Orientation"]))

        for child in children:
            if child.tag == "TX":
                tx = xmint_to_int(child.text)
            elif child.tag == "TY":
                ty = xmint_to_int(child.text)
            elif child.tag == "TW":
                tw = xmint_to_int(child.text)
            elif child.tag == "TH":
                th = xmint_to_int(child.text)

        return TabletPannel(tx, ty, tw, th, selected_orientation)




    # The menubar choice is (0°, 90°, 180°, 270°), so, selected orientation is 0, 1, 2 and 3
    @staticmethod
    def degree_to_id(degree_orientation):
        orientation_id = 0

        if degree_orientation == 0:
            orientation_id = 0

        elif degree_orientation == 90:
            orientation_id = 1

        elif degree_orientation == 180:
            orientation_id = 2

        elif degree_orientation == 270:
            orientation_id = 3

        return orientation_id



    # The menubar choice is (0°, 90°, 180°, 270°), so, selected orientation is 0, 1, 2 and 3
    @staticmethod
    def id_to_degree(orientation_id):
        orientation_degree = 0

        if orientation_id == 0:
            orientation_degree = 0

        elif orientation_id == 1:
            orientation_degree = 90

        elif orientation_id == 2:
            orientation_degree = 180

        elif orientation_id == 3:
            orientation_degree = 270

        return orientation_degree