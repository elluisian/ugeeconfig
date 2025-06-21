from ..utils.utils import *
from ..data.DesktopShortcutKeys import *
from .ButtonElement import *



class DesktopShortcutKeysElement(XMLElement):
    def writeToElement(self, data, parent=None):
        desktopscutkeys = data

        elem = XMLElement.handleTagWithParent("DesktopShortcutKeys", parent)

        XMLElement.append_simple_element("Fixed", bool_to_xmbool(desktopscutkeys.win_fixed), elem)
        XMLElement.append_simple_element("Zoom", float_to_xmfloat(desktopscutkeys.zoom), elem)
        XMLElement.append_simple_element("DisplayedAtCursor", bool_to_xmbool(desktopscutkeys.displayed_at_cursor), elem)
        XMLElement.append_simple_element("Rows", int_to_xmint(desktopscutkeys.row_no), elem)
        XMLElement.append_simple_element("Columns", int_to_xmint(desktopscutkeys.col_no), elem)


        vkeyselem = XMLElement.handleTagWithParent("VirtualKey", elem)

        for i in desktopscutkeys.vkeys:
             vke = VirtualKeyElement()
             vke.writeToElement(i, vkeyselem)

        return elem




    def readFromElement(self,  elem=None, version=None):
        dsk = DesktopShortcutKeys()

        if elem.tag != "DesktopShortcutKeys":
            raise InvalidXMLTag("Tag name \"%s\" is invalid for DesktopShortcutKeys" % (elem.tag,))


        children = list(elem)
        for child in children:
            if child.tag == "Fixed":
                dsk.win_fixed = xmbool_to_bool(child.text)

            elif child.tag == "Zoom":
                dsk.zoom = xmfloat_to_float(child.text)

            elif child.tag == "DisplayedAtCursor":
                dsk.displayed_at_cursor = xmbool_to_bool(child.text)

            elif child.tag == "Rows":
                dsk.row_no = xmint_to_int(child.text)

            elif child.tag == "Columns":
                dsk.col_no = xmint_to_int(child.text)

            elif child.tag == "VirtualKey":
                vkchildren = get_children(child)

                dsk.vkeys = {}
                for subch in vkchildren:
                    vke = VirtualKeyElement()
                    vkeyInst = vke.readFromElement(subch)
                    dsk.vkeys[vkeyInst.tag_no] = vkeyInst

            else:
                raise InvalidXMLTag("Tag name \"%s\" is invalid for element \"%s\"" % (child.tag, elem.tag,))


        return dsk