import re

from ..utils.XMLElement import *
from ..utils.utils import *
from ..data.Button import *

from .ActionElement import *



class VirtualKeyElement(XMLElement):
    def writeToElement(self, data, parent=None):
        virtualkey = data
        vkeyActData = virtualkey.getCustomActionData()

        elem = XMLElement.handleTagWithParent("K" + int_to_xmint(virtualkey.getTagNo()), parent)
        elem.attrib["id"] = bool_to_xmbool(vkeyActData.isEnabled())
        elem.attrib["Actid"] = int_to_xmint(virtualkey.getActid())

        actElement = ActionElement(vkeyActData)
        actElement.writeToElement(vkeyActData.getAction(), elem)

        return elem


    def readFromElement(self, elem=None, version=None):
        subch = elem
        m = subch.tag.find("K")
        if m > -1:
            tagno = xmint_to_int(subch.tag[m + 1:])
            idAttrib = xmbool_to_bool(subch.attrib["id"])
            actidAttrib = subch.attrib["Actid"]

            vkInst = VirtualKey(tagno, actidAttrib)
            vkCData = vkInst.getCustomActionData()

            actElement = ActionElement(vkCData)
            actInst = actElement.readFromElement(subch, version)
            vkCData.setAction(actInst)

            return vkInst

        else:
            raise InvalidXMLTag("Tag name \"%s\" is invalid" % (subch.tag,))




class TabletButtonElement(XMLElement):
    def __init__(self, showIds = True):
        self.showIds = showIds


    def writeToElement(self, data, parent=None):
        tabletbutton = data
        tbActData = tabletbutton.getCustomActionData()
        actionSet = tbActData.isEnabled()

        elem = XMLElement.handleTagWithParent("K" + int_to_xmint(tabletbutton.getTagNo()), parent)
        elem.attrib["id"] = bool_to_xmbool(tbActData.isEnabled())

        if self.showIds:
            elem.attrib["Motid"] = int_to_xmint(tabletbutton.getMotid())
            elem.attrib["Actid"] = int_to_xmint(tabletbutton.getActid())
            elem.attrib["Show"] = bool_to_xmbool(tabletbutton.getShow())

        actElement = ActionElement(tbActData)
        actElement.writeToElement(tbActData.getAction(), elem)

        return elem


    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        tagName = elem.tag
        tagNo = re.match("K([0-9]+)", elem.tag)
        tagNo = xmint_to_int(tagNo.group(1))
        actIdAttr = 0
        motIdAttr = 0
        showAttr = True


        if "Actid" in elem.attrib:
            actIdAttr = xmint_to_int(elem.attrib["Actid"])

        if "Motid" in elem.attrib:
            motIdAttr = xmint_to_int(elem.attrib["Motid"])

        if "Show" in elem.attrib:
            showAttr = xmbool_to_bool(elem.attrib["Show"])

        idAttrib = xmbool_to_bool(elem.attrib["id"])

        tbInst = TabletButton(tagNo, actIdAttr, motIdAttr, showAttr)
        tbActData = tbInst.getCustomActionData()
        tbActData.setEnabled(idAttrib)

        actElement = ActionElement(tbActData)
        actInst = actElement.readFromElement(elem, version)
        tbActData.setAction(actInst)

        return tbInst




class PenButtonElement(XMLElement):
    def writeToElement(self, data, parent=None):
        penbutton = data
        pbActData = penbutton.getCustomActionData()

        elem = XMLElement.handleTagWithParent("PenBtn" + int_to_xmint(penbutton.getTagNo()), parent)
        elem.attrib["id"] = bool_to_xmbool(pbActData.isEnabled())
        elem.attrib["Actid"] = int_to_xmint(penbutton.getActid())

        actElement = ActionElement(pbActData)
        actElement.writeToElement(pbActData.getAction(), elem)

        return elem


    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        tagName = elem.tag
        tagNo = re.match("PenBtn([0-9]+)", elem.tag)
        tagNo = xmint_to_int(tagNo.group(1))

        actIdAttrib = xmint_to_int(elem.attrib["Actid"])
        idAttrib = xmbool_to_bool(elem.attrib["id"])

        pnInst = PenButton(tagNo, actIdAttrib)
        pnActData = pnInst.getCustomActionData()
        actElement = ActionElement(pnActData)
        actInst = actElement.readFromElement(elem, version)
        pnActData.setAction(actInst)

        return pnInst





class WheelActMovementElement(XMLElement):
    def writeToElement(self, data, parent=None):
        wheelactmov = data
        whelActData = wheelactmov.getCustomActionData()

        elem = XMLElement.handleTagWithParent("W" + int_to_xmint(wheelactmov.getTagNo()), parent)
        usage = whelActData.getUsage()
        if usage == WHEEL_USG_DEFAULT:
            usage = 0
        elif usage == WHEEL_USG_NOP:
            usage = 1
        elif usage == WHEEL_USG_CUSTOM:
            usage = 2
        elem.attrib["id"] = int_to_xmint(usage)

        actElement = ActionElement(whelActData)
        actElement.writeToElement(None, elem) # data is useless in this case, everything is done thanks to whelActData

        return elem



    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        tagNo = re.match("W([0-9]+)", elem.tag)
        tagNo = xmint_to_int(tagNo.group(1))

        whelInst = WheelActMovement(tagNo)
        whelActData = whelInst.getCustomActionData()

        usage = xmint_to_int(elem.attrib["id"])
        if usage not in range(0, 3):
            usage = WHEEL_USG_DEFAULT
        elif usage == 0:
            usage = WHEEL_USG_DEFAULT
        elif usage == 1:
            usage = WHEEL_USG_NOP
        elif usage == 2:
            usage = WHEEL_USG_CUSTOM

        whelActData.setUsage(usage)

        actElement = ActionElement(whelActData)
        actElement.readFromElement(elem, version) # Again, not useful to assign, everything is done within whelActData

        return whelInst
