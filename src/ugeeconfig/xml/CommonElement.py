from ..utils.utils import *
from ..data.Common import *
from .ScreenMappingElement import *
from .TabletPannelElement import *
from .PictureFilesElement import *
from .SCElement import *





class CommonElement(XMLElement):
    def writeToElement(self, data, parent=None):
        common = data

        elem = XMLElement.handleTagWithParent("Common", parent)

        screenmappingel = ScreenMappingElement()
        screenmappingel.writeToElement(common.screenmapping, elem)

        tabletpannelel = TabletPannelElement()
        tabletpannelel.writeToElement(common.tabletpannel, elem)

        # Other
        XMLElement.append_simple_element("DisableInfo", bool_to_xmbool(not common.enable_messages), elem)
        XMLElement.append_simple_element("DisableQuickKey", bool_to_xmbool(not common.enable_tabletkeys), elem)
        XMLElement.append_simple_element("DisablePressure", bool_to_xmbool(not common.enable_pressure), elem)
        XMLElement.append_simple_element("DisableSlope", bool_to_xmbool(not common.enable_slope), elem)

        # PictureFiles
        picflel = PictureFilesElement()
        picflel.writeToElement(common.picturefiles, elem)

        if common.sc is not None:
            scel = SCElement()
            scel.writeToElement(common.sc, elem)

        return elem



    def readFromElement(self,  elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")

        if elem.tag != "Common":
            raise InvalidXMLTag("Element \"%s\" is invalid, \"Common\" expected!" % (elem.tag,))

        scrnmap = None
        tabpan = None
        disinfo = None
        disquick = None
        dispress = None
        disslope = None
        pictfiles = None
        sc = None

        children = get_children(elem)
        for child in children:
            if child.tag == "ScreenMapping":
                scel = ScreenMappingElement()
                scrnmap = scel.readFromElement(child, version)

            elif child.tag == "TabletPannel":
                tabel = TabletPannelElement()
                tabpan = tabel.readFromElement(child, version)

            elif child.tag == "DisableInfo":
                disinfo = xmbool_to_bool(child.text)

            elif child.tag == "DisableQuickKey":
                disquick = xmbool_to_bool(child.text)

            elif child.tag == "DisablePressure":
                dispress = xmbool_to_bool(child.text)

            elif child.tag == "DisableSlope":
                disslope = xmbool_to_bool(child.text)

            elif child.tag == "PictureFiles":
                pictel = PictureFilesElement()
                pictfiles = pictel.readFromElement(child, version)

            elif child.tag == "SC":
                scel = SCElement()
                sc = scel.readFromElement(child, version)

            else:
                raise InvalidXMLTag("Element \"%s\" is invalid during the analysis of \"Common\"!" % (child.tag,))


        return Common(scrnmap, tabpan, pictfiles, sc, not disinfo, not disquick, not dispress, not disslope)