# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from .utils.utils import *
from .data.DeviceInfo import *
from .data.PictureFiles import *
from .data.AppSettings import *
from .data.PressurePoints import *
from .data.Button import *
from .data.SC import *
from .data.ScreenMapping import *
from .data.TabletPannel import *
from .data.DesktopShortcutKeys import *
from .data.Device import *
from .data.Ring import *
from .data.Ugee import *






def generate_default_config():
    DEVICE_DATA = {}


    ##################
    # DEVICE "RB160" #
    ##################
    DEVNAME = "RB160"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 6, pentype = 0, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (209, 271, 106, 66),
        t1 = (232, 282, 36, 58),
        t2 = (184, 271, 106, 66),
        t3 = (232, 270, 36, 58)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    ####################
    # DEVICE "BP1003W" #
    ####################
    DEVNAME = "BP1003W"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 6, pentype = 11, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (209, 275, 104, 58),
        t1 = (233, 282, 33, 57),
        t2 = (186, 276, 104, 58),
        t3 = (233, 269, 33, 59)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    ####################
    # DEVICE "BPU1001" #
    ####################
    DEVNAME = "BPU1001"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 6, pentype = 4, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (205, 272, 118, 65),
        t1 = (231, 281, 37, 63),
        t2 = (177, 272, 118, 65),
        t3 = (231, 265, 37, 63)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_RCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    ####################
    # DEVICE "BPU1002" #
    ####################
    DEVNAME = "BPU1002"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 8, pentype = 0, trackpad = 0, control = 1)

    DEVPIC = PictureFiles(
        t0 = (208, 272, 107, 66),
        t1 = (232, 283, 36, 57),
        t2 = (184, 271, 107, 66),
        t3 = (232, 270, 36, 57)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLZ, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 7),
            TabletButton(tagno = 9, actid = ACTID_FUNCT_DISPIFACE, motid = 8),
        )
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    #################
    # DEVICE "M708" #
    #################
    DEVNAME = "M708"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 8, pentype = 0, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (201, 266, 121, 76),
        t1 = (229, 278, 41, 66),
        t2 = (177, 266, 121, 76),
        t3 = (229, 265, 41, 66)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLZ, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 7),
            TabletButton(tagno = 9, actid = ACTID_FUNCT_DISPIFACE, motid = 8),
        )
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    ####################
    # DEVICE "BPU0908" #
    ####################
    DEVNAME = "BPU0908"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 4, pentype = 5, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (206, 270, 105, 69),
        t1 = (231, 281, 37, 57),
        t2 = (188, 270, 105, 69),
        t3 = (231, 271, 37, 57)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 4),
        ),
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    ####################
    # DEVICE "BPH0908" #
    ####################
    DEVNAME = "BPH0908"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 4, pentype = 3, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (206, 270, 105, 69),
        t1 = (231, 281, 37, 57),
        t2 = (188, 270, 105, 69),
        t3 = (231, 271, 37, 57)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 4),
        ),
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "BPU0610W" #
    #####################
    DEVNAME = "BPU0610W"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 10, pentype = 3, trackpad = 0, control = 0, key_direction = 1)

    DEVPIC = PictureFiles(
        t0 = (200, 280, 103, 63),
        t1 = (228, 278, 36, 56),
        t2 = (197, 267, 103, 63),
        t3 = (236, 276, 36, 56)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_V, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLS, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLZ, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 8),
            TabletButton(tagno = 9, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 9),
            TabletButton(tagno = 10, actid = ACTID_FUNCT_DISPIFACE, motid = 10),
        ),
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "BPG1002L" #
    #####################
    DEVNAME = "BPG1002L"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 8, pentype = 8, trackpad = 0, control = 1)

    DEVPIC = PictureFiles(
        t0 = (218, 282, 78, 48),
        t1 = (224, 275, 50, 77),
        t2 = (205, 281, 78, 48),
        t3 = (225, 260, 50, 77)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_V, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLS, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLZ, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 8),
        ),
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    ######################
    # DEVICE "BPG1002L2" #
    ######################
    DEVNAME = "BPG1002L2"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 8, pentype = 11, trackpad = 0, control = 1)

    DEVPIC = PictureFiles(
        t0 = (218, 282, 78, 48),
        t1 = (224, 275, 50, 77),
        t2 = (205, 281, 78, 48),
        t3 = (225, 260, 50, 77)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLZ, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_FUNCT_DISPIFACE, motid = 8),
        ),
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    ####################
    # DEVICE "BPG0611" #
    ####################
    DEVNAME = "BPG0611"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 10, pentype = 0, trackpad = 0, control = 1, key_direction = 1)

    DEVPIC = PictureFiles(
        t0 = (211, 286, 78, 49),
        t1 = (220, 267, 51, 77),
        t2 = (211, 277, 78, 49),
        t3 = (230, 267, 50, 76)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_V, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLS, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLZ, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 8),
            TabletButton(tagno = 9, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 9),
            TabletButton(tagno = 10, actid = ACTID_FUNCT_DISPIFACE, motid = 10),
        ),
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    ####################
    # DEVICE "BPG1011" #
    ####################
    DEVNAME = "BPG1011"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 12, pentype = 0, trackpad = 0, control = 0, key_direction = 1)

    DEVPIC = PictureFiles(
        t0 = (205, 283, 89, 54),
        t1 = (219, 262, 56, 86),
        t2 = (207, 275, 89, 54),
        t3 = (227, 263, 55, 84)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = {"speed": 5, "enabled": False},
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 8),
            TabletButton(tagno = 9, actid = ACTID_FUNCT_DISPIFACE, motid = 9),
            TabletButton(tagno = 10, actid = ACTID_FUNCT_SWITCHMON, motid = 10),
            TabletButton(tagno = 11, actid = ACTID_KEYSTRK_V, motid = 11),
            TabletButton(tagno = 12, actid = ACTID_KEYSTRK_CTRLO, motid = 12),
        ),
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())





    #################
    # DEVICE "UD13" #
    #################
    DEVNAME = "UD13"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 6, pentype = 0, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (197, 271, 110, 67),
        t1 = (231, 275, 37, 62),
        t2 = (192, 271, 110, 67),
        t3 = (231, 274, 37, 62)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_CTRLZ, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_FUNCT_DISPIFACE, motid = 6),
        ),
        # No ring apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "LPH1101F" #
    #####################
    DEVNAME = "LPH1101F"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 6, pentype = 4, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (203, 273, 116, 63),
        t1 = (232, 279, 35, 64),
        t2 = (180, 273, 116, 63),
        t3 = (232, 268, 35, 64)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_CTRLZ, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_FUNCT_DISPIFACE, motid = 6),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "LPU1503" #
    #####################
    DEVNAME = "LPU1503"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 8, pentype = 12, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (197, 273, 112, 62),
        t1 = (231, 277, 35, 61),
        t2 = (191, 273, 112, 62),
        t3 = (231, 273, 35, 61)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_FUNCT_DISPIFACE, motid = 6),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())












    #####################
    # DEVICE "LPU1501" #
    #####################
    DEVNAME = "LPU1501"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 6, pentype = 11, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (197, 271, 110, 67),
        t1 = (231, 275, 37, 62),
        t2 = (192, 271, 110, 67),
        t3 = (231, 274, 37, 62)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_CTRLZ, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_FUNCT_DISPIFACE, motid = 6),
        ),
        # No rings apparently
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())







    #####################
    # DEVICE "LPU2202" #
    #####################
    DEVNAME = "LPU2202"

    DEVINFO = DeviceInfo(ringnum = 2, keynum = 20, pentype = 12, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (185, 266, 132, 74),
        t1 = (229, 269, 41, 74),
        t2 = (184, 269, 132, 74),
        t3 = (229, 268, 41, 74)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 8),
            TabletButton(tagno = 9, actid = ACTID_FUNCT_DISPIFACE, motid = 9),
            TabletButton(tagno = 10, actid = ACTID_FUNCT_SWRING1, motid = 10),
            TabletButton(tagno = 11, actid = ACTID_FUNCT_SWITCHMON, motid = 11),
            TabletButton(tagno = 12, actid = ACTID_KEYSTRK_V, motid = 12),
            TabletButton(tagno = 13, actid = ACTID_KEYSTRK_L, motid = 13),
            TabletButton(tagno = 14, actid = ACTID_KEYSTRK_CTRLO, motid = 14),
            TabletButton(tagno = 15, actid = ACTID_KEYSTRK_CTRLN, motid = 15),
            TabletButton(tagno = 16, actid = ACTID_KEYSTRK_CTRLSHIFTN, motid = 16),
            TabletButton(tagno = 17, actid = ACTID_KEYSTRK_CTRLE, motid = 17),
            TabletButton(tagno = 18, actid = ACTID_KEYSTRK_F, motid = 18),
            TabletButton(tagno = 19, actid = ACTID_KEYSTRK_CTRLC, motid = 19),
            TabletButton(tagno = 20, actid = ACTID_KEYSTRK_CTRLV, motid = 20),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),
        Ring("R2", 0, 0, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())




    #####################
    # DEVICE "P22Pro" #
    #####################
    DEVNAME = "P22Pro"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 0, pentype = 11, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (176, 261, 148, 76),
        t1 = (234, 265, 39, 81),
        t2 = (175, 272, 148, 76),
        t3 = (229, 265, 39, 81)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        # No keys
        # No rings
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())






    #####################
    # DEVICE "LAU2202" #
    #####################
    DEVNAME = "LAU2202"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 16, pentype = 11, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (182, 261, 136, 78),
        t1 = (230, 268, 43, 74),
        t2 = (181, 269, 136, 78),
        t3 = (226, 267, 43, 74)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 8),
            TabletButton(tagno = 9, actid = ACTID_FUNCT_DISPIFACE, motid = 9),
            TabletButton(tagno = 10, actid = ACTID_FUNCT_SWITCHMON, motid = 10),
            TabletButton(tagno = 11, actid = ACTID_KEYSTRK_V, motid = 11),
            TabletButton(tagno = 12, actid = ACTID_KEYSTRK_CTRLO, motid = 12),
            TabletButton(tagno = 13, actid = ACTID_KEYSTRK_CTRLN, motid = 13),
            TabletButton(tagno = 14, actid = ACTID_KEYSTRK_CTRLSHIFTN, motid = 14),
            TabletButton(tagno = 15, actid = ACTID_KEYSTRK_CLBRK, motid = 15),
            TabletButton(tagno = 16, actid = ACTID_KEYSTRK_OPBRK, motid = 16),
        ),
        # No rings
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())




    #####################
    # DEVICE "LPU1102" #
    #####################
    DEVNAME = "LPU1102"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 8, pentype = 12, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (213, 282, 83, 46),
        t1 = (226, 269, 48, 82),
        t2 = (206, 282, 83, 46),
        t3 = (226, 260, 48, 82)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_FUNCT_DISPIFACE, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_FUNCT_SWRING1, motid = 8),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
            WheelActMovement(tagno = 5),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "LPU1302F" #
    #####################
    DEVNAME = "LPU1302F"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 8, pentype = 12, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (197, 273, 112, 62),
        t1 = (231, 277, 35, 61),
        t2 = (191, 273, 112, 62),
        t3 = (231, 273, 35, 61)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_FUNCT_DISPIFACE, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_FUNCT_SWRING1, motid = 8),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "LPU1505F" #
    #####################
    DEVNAME = "LPU1505F"

    DEVINFO = DeviceInfo(ringnum = 2, keynum = 8, pentype = 13, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (195, 271, 123, 68),
        t1 = (231, 275, 37, 68),
        t2 = (182, 270, 122, 68),
        t3 = (231, 267, 37, 68)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_FUNCT_DISPIFACE, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_FUNCT_SWRING1, motid = 8),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),
        Ring("TR", 0, 0, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "LPU2402Q" #
    #####################
    DEVNAME = "LPU2402Q"

    DEVINFO = DeviceInfo(ringnum = 2, keynum = 20, pentype = 12, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (185, 266, 132, 74),
        t1 = (229, 269, 41, 74),
        t2 = (184, 269, 132, 74),
        t3 = (229, 268, 41, 74)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 8),
            TabletButton(tagno = 9, actid = ACTID_FUNCT_DISPIFACE, motid = 9),
            TabletButton(tagno = 10, actid = ACTID_FUNCT_SWRING1, motid = 10),
            TabletButton(tagno = 11, actid = ACTID_FUNCT_SWITCHMON, motid = 11),
            TabletButton(tagno = 12, actid = ACTID_KEYSTRK_V, motid = 12),
            TabletButton(tagno = 13, actid = ACTID_KEYSTRK_L, motid = 13),
            TabletButton(tagno = 14, actid = ACTID_KEYSTRK_CTRLO, motid = 14),
            TabletButton(tagno = 15, actid = ACTID_KEYSTRK_CTRLN, motid = 15),
            TabletButton(tagno = 16, actid = ACTID_KEYSTRK_CTRLSHIFTN, motid = 16),
            TabletButton(tagno = 17, actid = ACTID_KEYSTRK_CTRLE, motid = 17),
            TabletButton(tagno = 18, actid = ACTID_KEYSTRK_F, motid = 18),
            TabletButton(tagno = 19, actid = ACTID_KEYSTRK_CTRLC, motid = 19),
            TabletButton(tagno = 20, actid = ACTID_KEYSTRK_CTRLV, motid = 20),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),
        Ring("R2", 0, 0, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "LPU1211F" #
    #####################
    DEVNAME = "LPU1211F"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 0, pentype = 10, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (204, 282, 93, 49),
        t1 = (223, 261, 54, 88),
        t2 = (204, 278, 93, 49),
        t3 = (223, 260, 54, 88)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        # No tablet buttons
        # No rings
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "LPU1611F" #
    #####################
    DEVNAME = "LPU1611F"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 0, pentype = 10, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (204, 282, 93, 49),
        t1 = (223, 261, 54, 88),
        t2 = (204, 278, 93, 49),
        t3 = (223, 260, 54, 88)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        # No tablet buttons
        # No rings
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())






    #####################
    # DEVICE "LA1501F" #
    #####################
    DEVNAME = "LA1501F"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 0, pentype = 11)

    DEVPIC = PictureFiles(
        t0 = (185, 268, 130, 72),
        t1 = (230, 270, 40, 70),
        t2 = (184, 268, 130, 72),
        t3 = (230, 270, 40, 70)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_MOUSEK_SCLICK),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLZ, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_FUNCT_DISPIFACE, motid = 8),
        ),
        # No rings
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())






    #####################
    # DEVICE "Q8W" #
    #####################
    DEVNAME = "Q8W"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 0, pentype = 7, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (203, 268, 105, 73),
        t1 = (229, 280, 40, 56),
        t2 = (193, 267, 105, 73),
        t3 = (230, 271, 40, 56)
    )

    TABLEPC = True

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (), # No pens
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLZ, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_FUNCT_DISPIFACE, motid = 8),
        ),
        # No rings
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "Q6" #
    #####################
    DEVNAME = "Q6"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 6, pentype = 2, trackpad = 0, control = 0, key_direction = 1)

    DEVPIC = PictureFiles(
        t0 = (205, 286, 92, 52),
        t1 = (232, 280, 27, 50),
        t2 = (202, 271, 92, 52),
        t3 = (241, 279, 27, 50)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (), # No pens
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_CTRLSHIFTZ, motid = 6),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_CTRLZ, motid = 5),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_CLBRK, motid = 4),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_OPBRK, motid = 3),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_B, motid = 1),
        ),
        # No rings
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())






    #####################
    # DEVICE "M808" #
    #####################
    DEVNAME = "M808"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 8, pentype = 1, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (207, 274, 100, 63),
        t1 = (233, 281, 33, 53),
        t2 = (194, 272, 100, 63),
        t3 = (234, 275, 33, 54)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_FUNCT_PENERSR),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_CTRLZ, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 6),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_ALT, motid = 7),
            TabletButton(tagno = 6, actid = ACTID_FUNCT_DISPIFACE, motid = 8),
        ),
        # No rings
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())




    #####################
    # DEVICE "M808" #
    #####################
    DEVNAME = "M908"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 8, pentype = 1, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (207, 274, 97, 61),
        t1 = (233, 281, 33, 53),
        t2 = (196, 274, 97, 61),
        t3 = (234, 275, 33, 54)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_FUNCT_PENERSR),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_FUNCT_SWRING1, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_FUNCT_DISPIFACE, motid = 8),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),),
    )

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, None, ScreenMapping.default(), TabletPannel.default())






    #####################
    # DEVICE "E12" #
    #####################
    DEVNAME = "E12"

    DEVINFO = DeviceInfo(ringnum = 0, keynum = 8, pentype = 1, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (207, 274, 100, 63),
        t1 = (233, 281, 33, 53),
        t2 = (194, 272, 100, 63),
        t3 = (234, 275, 33, 54)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_FUNCT_PENERSR),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_OPBRK, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_CLBRK, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_B, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_CTRLZ, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLSHIFTZ, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_E, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLMINUS, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLPLUS, motid = 8),
        ),
        # No rings
    )

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())





    #####################
    # DEVICE "E12PLUS" #
    #####################
    DEVNAME = "E12PLUS"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 8, pentype = 1, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (207, 274, 97, 61),
        t1 = (233, 281, 33, 53),
        t2 = (196, 274, 97, 61),
        t3 = (234, 275, 33, 54)
    )

    TABLEPC = True

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_FUNCT_PENERSR),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_OPBRK, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_CLBRK, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLOPBRK, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLCLBRK, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_KEYSTRK_CTRLZ, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_KEYSTRK_CTRLSHIFTZ, motid = 8),
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, ScreenMapping.default(), TabletPannel.default())






    #################
    # DEVICE "UE16" #
    # https://www.ugee.com/download/ue16 #
    #######################################
    DEVNAME = "UE16"

    DEVINFO = DeviceInfo(ringnum = 1, keynum = 9, pentype = 15, trackpad = 0, control = 0)

    DEVPIC = PictureFiles(
        t0 = (205, 274, 101, 58),
        t1 = (235, 281, 31, 55),
        t2 = (195, 276, 101, 58),
        t3 = (235, 275, 31, 55),
    )

    TABLEPC = False

    APP_SETTINGS = AppSettings(
        pressurepoints = PressurePoints.default(),
        tablepc = TABLEPC,
        relativecoords = AppSettings.defaultRelativeCoords(),
        penbtns = (
            PenButton(tagno = 0, actid = ACTID_FUNCT_ERSR),
            PenButton(tagno = 1, actid = ACTID_MOUSEK_RCLICK),
            PenButton(tagno = 2, actid = ACTID_FUNCT_PENERSR),
        ),
        tabletbtns = (
            TabletButton(tagno = 1, actid = ACTID_KEYSTRK_B, motid = 1),
            TabletButton(tagno = 2, actid = ACTID_KEYSTRK_E, motid = 2),
            TabletButton(tagno = 3, actid = ACTID_KEYSTRK_ALT, motid = 3),
            TabletButton(tagno = 4, actid = ACTID_KEYSTRK_SPACE, motid = 4),
            TabletButton(tagno = 5, actid = ACTID_KEYSTRK_CTRLS, motid = 5),
            TabletButton(tagno = 6, actid = ACTID_KEYSTRK_CTRLZ, motid = 6),
            TabletButton(tagno = 7, actid = ACTID_FUNCT_DISPIFACE, motid = 7),
            TabletButton(tagno = 8, actid = ACTID_FUNCT_DESKKEYS, motid = 8),
            TabletButton(tagno = 9, actid = ACTID_FUNCT_DESKKEYS, motid = 9, show=False)
        ),
        rings = (Ring("R", 0, None, (
            WheelActMovement(tagno = 1),
            WheelActMovement(tagno = 2),
            WheelActMovement(tagno = 3),
            WheelActMovement(tagno = 4),
        )),)
    )

    SC_ = SC(fKX = 1, fYLC = 1, fXLC = 1, fKY = 1)

    SCREEN_MAPPING = ScreenMapping(x = 0, y = 0, w = 1920, h = 1080, selected_res_opt = 2)

    TABLET_PANNEL = TabletPannel(x = 0, y = 0, w = 1342, h = 755, orientation = 0)

    DEVICE_DATA[DEVNAME] = Device.makeDevice(DEVNAME, DEVINFO, DEVPIC, APP_SETTINGS, SC_, SCREEN_MAPPING, TABLET_PANNEL)



    DESKTOPSCUT_KEYS = DesktopShortcutKeys.makeDefault(win_fixed = False, zoom = 1.0, displayedAtCursor = True, row_no = 1, col_no = 4,
        vkeys = (
            VirtualKey(tagno = 1, actid = ACTID_KEYSTRK_CTRLSHIFTZ),
            VirtualKey(tagno = 2, actid = ACTID_KEYSTRK_CTRLALTZ),
            VirtualKey(tagno = 3, actid = ACTID_KEYSTRK_CTRLSHIFTN),
            VirtualKey(tagno = 4, actid = ACTID_KEYSTRK_CTRLE),
            VirtualKey(tagno = 5, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 6, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 7, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 8, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 9, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 10, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 11, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 12, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 13, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 14, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 15, actid = ACTID_DRV_NOP),
            VirtualKey(tagno = 16, actid = ACTID_DRV_NOP),
        )
    )



    return Ugee(DEVICE_DATA, DESKTOPSCUT_KEYS)
