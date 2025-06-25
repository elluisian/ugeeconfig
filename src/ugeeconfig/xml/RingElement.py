from ..data.Ring import *
from .ButtonElement import *



class RingElement(XMLElement):
    def writeToElement(self, data, parent=None):
        ring = data

        el = etree.SubElement(parent, ring.tag_name)
        if ring.mode is not None:
            el.attribs["mode"] = int_to_xmint(ring.mode)

        el.attribs["id"] = int_to_xmint(ring.getSelectedWheel())

        wheelacts = ring.getWheelActMovemenets()

        for wact in wheelacts:
            wel = WheelActMovementElement()
            wel.writeElement(wact, el)

        return el




    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")


        wheelactbtns = []
        tag_name = elem.tag

        if "id" in elem.attrib:
            selected_wheel = xmint_to_int(elem.attrib["id"])
        else:
            selected_wheel = None

        if "mode" in elem.attrib:
            mode = xmint_to_int(elem.attrib["mode"])
        else:
            mode = None

        wchildren = get_children(elem)
        for wchild in wchildren:
            wel = WheelActMovementElement()
            wheelb = wel.readFromElement(wchild, version)
            wheelactbtns.append(wheelb)

        return Ring(tag_name, selected_wheel, mode, wheelactbtns)