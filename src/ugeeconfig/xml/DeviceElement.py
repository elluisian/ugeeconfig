from ..utils.utils import *
from ..data.Device import *
from .DeviceInfoElement import *
from .CommonElement import *
from .AppElement import *


class DeviceElement(XMLElement):
    def writeToElement(self, data, parent=None):
        device = data

        elem = XMLElement.handleTagWithParent(device.name, parent)

        #print(device.name)

        devinfoel = DeviceInfoElement()
        devinfoel.writeToElement(device.deviceinfo, elem)

        commel = CommonElement()
        commel.writeToElement(device.common, elem)

        commappel = AppElement()
        commappel.writeToElement(device.commonapp, elem)

        el = etree.SubElement(elem, "Apps")

        for i in device.apps:
            appel = AppElement()
            appel.writeToElement(i, el)

        return elem




    def readFromElement(self,  elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        name = elem.tag
        devinfo = None
        common = None
        commapp = None
        apps = []


        children = get_children(elem)

        for child in children:
            if child.tag == "DeviceInfo":
                devinfel = DeviceInfoElement()
                devinfo = devinfel.readFromElement(child, version)

            elif child.tag == "Common":
                commel = CommonElement()
                common = commel.readFromElement(child, version)

            elif child.tag == "CommonAPP":
                commappel = AppElement()
                commapp = commappel.readFromElement(child, version)

            elif child.tag == "Apps":
             appchildren = get_children(child)
             for appchild in appchildren:
                 currappel = AppElement()
                 currapp = currappel.readFromElement(appchild, version)
                 apps.append(currapp)

            else:
                 raise InvalidXMLTag("Element \"%s\" is invalid during the analysis of \"%s\"" % (child.tag, elem.tag,))

        return Device(name, devinfo, common, commapp, apps)
