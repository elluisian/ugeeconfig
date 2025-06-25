# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



import re

from ..utils.utils import *
from ..data.PressurePoints import *
from ..data.AppSettings import *
from .RingElement import *
from .PressurePointsElement import *
from .ButtonElement import *




class AppSettingsElement(XMLElement):
    def __init__(self, show_k_ids = True):
        self.show_k_ids = show_k_ids




    def writeToElement(self, data, parent=None):
        appsettings = data

        el = etree.SubElement(parent, "Pen")

        for i in appsettings.penbtns:
            pel = PenButtonElement()
            pel.writeToElement(i, el)

        ppoints = PressurePointsElement()
        ppoints.writeToElement(appsettings.pressurepoints, el)

        XMLElement.append_simple_element("TablePC", bool_to_xmbool(appsettings.tablepc), el)
        XMLElement.append_simple_element("RelativeCoords", bool_to_xmbool(appsettings.relativecoords.enabled), el, (("Speed", int_to_xmint(appsettings.relativecoords.speed)),))

        el = etree.SubElement(parent, "K")
        for i in appsettings.tabletbtns:
            tel = TabletButtonElement(self.show_k_ids)
            tel.writeToElement(i, el)

        for ringInst in appsettings.getRings():
            el = etree.SubElement(parent, ringInst.tag_name)

            if ringInst.selected_wheel is not None:
                el.attrib["id"] = int_to_xmint(ringInst.selected_wheel)

            if ringInst.mode is not None:
                el.attrib["mode"] = int_to_xmint(ringInst.mode)

            for btn in ringInst.wheel_actmovements:
                rbel = WheelActMovementElement()
                rbel.writeToElement(btn, el)

        return parent




    def readFromElement(self, elem=None, version=None):
        if elem is None:
            raise InvalidXMLTag("Element is None!")


        tablepc = None
        penbtns = []
        tabletbtns = []
        selected_wheelbtn = None
        wheelbtns = []
        rings = []
        p0 = None
        p1x = None
        p1y = None
        p2 = None


        children = get_children(elem)
        for child in children:
            if child.tag == "path":
                pass # Do nothing, already processed in AppIdElement


            elif child.tag == "Pen":
                penchildren = get_children(child)
                for penchild in penchildren:
                    if penchild.tag.startswith("PenBtn"):
                        pel = PenButtonElement()
                        penbtn = pel.readFromElement(penchild)
                        penbtns.append(penbtn)

                    elif penchild.tag == "P0":
                        p0 = xmfloat_to_float(penchild.text)

                    elif penchild.tag == "P1X":
                        p1x = xmfloat_to_float(penchild.text)

                    elif penchild.tag == "P1Y":
                        p1y = xmfloat_to_float(penchild.text)

                    elif penchild.tag == "P2":
                        p2 = xmfloat_to_float(penchild.text)

                    elif penchild.tag == "TablePC":
                        tablepc = xmbool_to_bool(penchild.text)

                    elif penchild.tag == "RelativeCoords":
                        relspeed = xmint_to_int(penchild.attrib["Speed"])
                        relenabled = xmbool_to_bool(penchild.text)


            elif child.tag == "K":
                kchildren = get_children(child)
                for kchild in kchildren:
                    tel = TabletButtonElement()
                    tbtn = tel.readFromElement(kchild, version)
                    tabletbtns.append(tbtn)


            # Various types of rings
            elif child.tag in ("R", "R2", "TR",):
                rel = RingElement()
                ringInst = rel.readFromElement(child, version)
                rings.append(ringInst)

            else:
                raise InvalidXMLTag("Element \"%s\" is invalid during the analysis of the app settings (under \"CommonApp\" or under \"app\")!" % (child.tag,))


        pressurepoints = PressurePoints(p0, Point(p1x, p1y), p2)
        relativecoords = {"enabled": relenabled, "speed": relspeed}


        return AppSettings(pressurepoints, tablepc, relativecoords, penbtns, tabletbtns, rings)
