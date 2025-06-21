import math

from .Prop import *
from ..data.Action import getActIdFromValue









def __get_common(device):
    return Prop.UGEE_INST.getPentable(device).getCommon()

def __get_commonapp_settings(device):
     return Prop.UGEE_INST.getPentable(device).getCommonApp().getSettings()

def __get_deskshortcutkeys():
    return Prop.UGEE_INST.getDesktopShortcutKeys()

def __get_penbtn(device, penbtn):
    return __get_commonapp_settings(device).getPenBtn(penbtn)

def __get_tabkey(device, tabkey):
    return __get_commonapp_settings(device).getTabletBtn(tabkey)

def __get_wheelactmov(device, ringName, wheelbtn):
    return __get_commonapp_settings(device).getRingByTagName(ringName).getWheelActMovementByTagNo(wheelbtn)

def __get_vkey(vkeyName):
    return __get_deskshortcutkeys().getVKeyByTagNo(vkeyName)

def __get_actid(entity):
    actval = getActIdFromValue(entity.getActid())

    if actval is None:
        raise ValueInvalidActidException("Error: value \"%s\" is not a valid actid!" % (str(value.v),))

    return actval[1]

def __set_actid(entity, value):
    actval = getActIdFromValue(value.v)

    if actval is None:
        raise ValueInvalidActidException("Error: value \"%s\" is not a valid actid!" % (str(value.v),))

    entity.setActid(actval[1])

def __get_customactdata(entity):
    return entity.getCustomActionData()










def generic_formatter(path, val, isSet=False):
    if isSet:
        return "%s = %s" % (path, val,)
    else:
        return "%s: %s" % (path, val,)



def actid_formatter(path, val, isSet):
    actiddata = getActIdFromValue(val)

    if actiddata is not None:
        if isSet:
            return "%s = %s (%s)" % (path, actiddata[0], actiddata[1],)
        else:
            return "%s: %s (%s)" % (path, actiddata[0], actiddata[1],)

    return generic_formatter(path, val, isSet)





def set_pentilt(params, v):
    device = params[0]
    __get_common(device).enable_slope = v.v

def get_pentilt(params):
    device = params[0]
    return __get_common(device).enable_slope



def set_penpressure(params, v):
    device = params[0]
    __get_common(device).enable_pressure = v.v

def get_penpressure(params):
    device = params[0]
    return __get_common(device).enable_pressure



def set_penpressure_points(params, v):
    device = params[0]
    __get_commonapp_settings(device).pressurepoints = v.v

def get_penpressure_points(params):
    device = params[0]
    return __get_commonapp_settings(device).pressurepoints



def set_mousemode(params, v):
    device = params[0]
    __get_commonapp_settings(device).relativecoords.enabled = v.v

def get_mousemode(params):
    device = params[0]
    return __get_commonapp_settings(device).relativecoords.enabled



def set_mousemode_speed(params, v):
    device = params[0]
    if v.v < 1 or v.v > 10:
        v.v = 5
    __get_commonapp_settings(device).relativecoords.speed = v.v

def get_mousemode_speed(params):
    device = params[0]
    return __get_commonapp_settings(device).relativecoords.speed



def set_screenres(params, v):
    device = params[0]
    return __get_common(device).screenmapping.assignFromRectangle(v.v)

def get_screenres(params):
    device = params[0]
    return __get_common(device).screenmapping



def set_tabletres(params, v):
    device = params[0]
    __get_common(device).tabletpannel.assignFromRectangle(v.v)

def get_tabletres(params):
    device = params[0]
    return __get_common(device).tabletpannel



def set_tabletrot(params, v):
    device = params[0]
    tabp = __get_common(device).tabletpannel

    if v.v != 0 and v.v != 90 and v.v != 180 and v.v != 270:
        v.v = 0

    tabp.orientation = v.v

def get_tabletrot(params):
    device = params[0]
    tabp = __get_common(device).tabletpannel
    return tabp.orientation



def set_showmessages(params):
    device = params[0]
    __get_common(device).enable_messages = v.v

def get_showmessages(params):
    device = params[0]
    return __get_common(device).enable_messages



def set_tabletkeys(params, v):
    device = params[0]
    __get_common(device).enable_tabletkeys = v.v

def get_tabletkeys(params):
    device = params[0]
    return __get_common(device).enable_tabletkeys



def set_deskkeys_fixed(params, v):
    __get_deskshortcutkeys().win_fixed = v.v

def get_deskkeys_fixed(params):
    return __get_deskshortcutkeys().win_fixed



def set_deskkeys_zoom(params, v):
    if v.v != 1 and v.v != 1.5 and v.v != 2:
        v.v = 1
    __get_deskshortcutkeys().zoom = v.v

def get_deskkeys_zoom(params):
    return __get_deskshortcutkeys().zoom



def set_deskkeys_nokeys(params, v):
    if v.v < 0 or v.v > 16:
        v.v = 0

    row = 0
    col = 0
    # A line is composed of 4 columns
    if v.v > 0:
        row = math.ceil(v.v / 4)
        col = v.v - ((row - 1) * 4)

    deskkeys = __get_deskshortcutkeys()
    deskkeys.row_no = row
    deskkeys.col_no = col

def get_deskkeys_nokeys(params):
    deskkeys = __get_deskshortcutkeys()
    return deskkeys.row_no * deskkeys.col_no





##################
## Multi Groups ##
##################
def multiget_devices(params):
    return Prop.UGEE_INST.getAvailableDevices()

def multiget_devices_expected(available):
    return list(available)



def multiget_pen_buttons(params):
    device = params[0]
    return __get_commonapp_settings(device).getPenBtnNames()

def multiget_pen_buttons_expected(available):
    return list(map(lambda x : "button" + str(x), available))

def multiget_pen_buttons_extract(btnname):
    return int(btnname[len("button"):])



def multiget_tablet_keys(params):
    device = params[0]
    return __get_commonapp_settings(device).getTabletBtnNames()

def multiget_tablet_keys_expected(available):
    return list(map(lambda x : "key" + str(x), available))

def multiget_tablet_keys_extract(keyname):
    return int(keyname[len("key"):])



def multiget_tablet_rings(params):
    device = params[0]
    return __get_commonapp_settings(device).getRingNames()

def multiget_tablet_rings_expected(available):
    return list(available)



def multiget_ring_wheel_movements(params):
    device = params[0]
    ring = params[1]
    return __get_commonapp_settings(device).getRingByTagName(ring).getWheelActMovementNames()

def multiget_ring_wheel_movements_expected(available):
    return list(map(lambda x : "wheel_movement" + str(x), available))

def multiget_ring_wheel_movements_extract(wheelname):
    return int(wheelname[len("wheel_movement"):])



def multiget_deskkeys_vkeys(params):
    return __get_deskshortcutkeys().getVKeysNames()

def multiget_deskkeys_vkeys_expected(available):
    return list(map(lambda x : "vkey" + str(x), available))

def multiget_deskkeys_vkeys_extract(vkeyname):
    return int(vkeyname[len("vkey"):])





#####################
## Set/Get actions ##
#####################
## PEN BUTTONS
def multiple_pen_button_set_default_action(params, v):
    device = params[0]
    penbtn = multiget_pen_buttons_extract(params[1])
    __set_actid(__get_penbtn(device, penbtn), v)

def multiple_pen_button_get_default_action(params):
    device = params[0]
    penbtn = multiget_pen_buttons_extract(params[1])
    return __get_actid(__get_penbtn(device, penbtn))



def multiple_pen_button_set_custom_action(params, v):
    device = params[0]
    penbtn = multiget_pen_buttons_extract(params[1])
    __get_customactdata(__get_penbtn(device, penbtn)).setAction(v.v)

def multiple_pen_button_get_custom_action(params):
    device = params[0]
    penbtn = multiget_pen_buttons_extract(params[1])
    return __get_customactdata(__get_penbtn(device, penbtn)).getAction()



def multiple_pen_button_set_custom_action_label(params, v):
    device = params[0]
    penbtn = multiget_pen_buttons_extract(params[1])
    __get_customactdata(__get_penbtn(device, penbtn)).setLabel(v.v)

def multiple_pen_button_get_custom_action_label(params):
    device = params[0]
    penbtn = multiget_pen_buttons_extract(params[1])
    return __get_customactdata(__get_penbtn(device, penbtn)).getLabel()



def multiple_pen_button_set_custom_action_enabled(params, v):
    device = params[0]
    penbtn = multiget_pen_buttons_extract(params[1])
    __get_customactdata(__get_penbtn(device, penbtn)).setEnabled(v.v)

def multiple_pen_button_get_custom_action_enabled(params):
    device = params[0]
    penbtn = multiget_pen_buttons_extract(params[1])
    return __get_customactdata(__get_penbtn(device, penbtn)).isEnabled()



## TABLET KEYS
def multiple_tablet_key_set_default_action(params, v):
    device = params[0]
    tabkey = multiget_tablet_keys_extract(params[1])
    __set_actid(__get_tabkey(device, tabkey), v)

def multiple_tablet_key_get_default_action(params):
    device = params[0]
    tabkey = multiget_tablet_keys_extract(params[1])
    return __get_actid(__get_tabkey(device, tabkey))



def multiple_tablet_key_set_custom_action(params, v):
    device = params[0]
    tabkey = multiget_tablet_keys_extract(params[1])
    __get_customactdata(__get_tabkey(device, tabkey)).setAction(v.v)

def multiple_tablet_key_get_custom_action(params):
    device = params[0]
    tabkey = multiget_tablet_keys_extract(params[1])
    return __get_customactdata(__get_tabkey(device, tabkey)).getAction()



def multiple_tablet_key_set_custom_action_label(params, v):
    device = params[0]
    tabkey = multiget_tablet_keys_extract(params[1])
    __get_customactdata(__get_tabkey(device, tabkey)).setLabel(v.v)

def multiple_tablet_key_get_custom_action_label(params):
    device = params[0]
    tabkey = multiget_tablet_keys_extract(params[1])
    return __get_customactdata(__get_tabkey(device, tabkey)).getLabel()



def multiple_tablet_key_set_custom_action_enabled(params, v):
    device = params[0]
    tabkey = multiget_tablet_keys_extract(params[1])
    __get_customactdata(__get_tabkey(device, tabkey)).setEnabled(v.v)

def multiple_tablet_key_get_custom_action_enabled(params):
    device = params[0]
    tabkey = multiget_tablet_keys_extract(params[1])
    return __get_customactdata(__get_tabkey(device, tabkey)).isEnabled()



# WHEEL MOVEMENT
def multiple_ring_wheelmov_set_custom_ccwaction(params, v):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).setCCWAction(v.v)

def multiple_ring_wheelmov_get_custom_ccwaction(params):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    return __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).getCCWAction()



def multiple_ring_wheelmov_set_custom_ccwaction_label(params, v):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).setCCWLabel(v.v)

def multiple_ring_wheelmov_get_custom_ccwaction_label(params):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    return __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).getCCWLabel()



def multiple_ring_wheelmov_set_custom_cwaction(params, v):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).setCWAction(v.v)

def multiple_ring_wheelmov_get_custom_cwaction(params):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    return __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).getCWAction()



def multiple_ring_wheelmov_set_custom_cwaction_label(params, v):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).setCWLabel(v.v)

def multiple_ring_wheelmov_get_custom_cwaction_label(params):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    return __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).getCWLabel()



def multiple_ring_wheelmov_set_usage(params, v):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).setUsage(v.v)

def multiple_ring_wheelmov_get_usage(params):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    return __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).getUsage()



def multiple_ring_wheelmov_set_label(params, v):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).setLabel(v.v)

def multiple_ring_wheelmov_get_label(params):
    device = params[0]
    ringName = params[1]
    wheelbtn = multiget_ring_wheel_movements_extract(params[2])
    return __get_customactdata(__get_wheelactmov(device, ringName, wheelbtn)).getLabel()



# DESK KEYS
def multiple_deskkeys_vkeys_set_default_action(params, v):
    vkeyName = multiget_deskkeys_vkeys_extract(params[0])
    __set_actid(__get_vkey(vkeyName), v)

def multiple_deskkeys_vkeys_get_default_action(params):
    vkeyName = multiget_deskkeys_vkeys_extract(params[0])
    return __get_actid(__get_vkey(vkeyName))



def multiple_deskkeys_vkeys_set_custom_action(params, v):
    vkeyName = multiget_deskkeys_vkeys_extract(params[0])
    __get_customactdata(__get_vkey(vkeyName)).setAction(v.v)

def multiple_deskkeys_vkeys_get_custom_action(params):
    vkeyName = multiget_deskkeys_vkeys_extract(params[0])
    return __get_customactdata(__get_vkey(vkeyName)).getAction()



def multiple_deskkeys_vkeys_set_custom_action_label(params, v):
    vkeyName = multiget_deskkeys_vkeys_extract(params[0])
    __get_customactdata(__get_vkey(vkeyName)).setLabel(v.v)

def multiple_deskkeys_vkeys_get_custom_action_label(params):
    vkeyName = multiget_deskkeys_vkeys_extract(params[0])
    return __get_customactdata(__get_vkey(vkeyName)).getLabel()



def multiple_deskkeys_vkeys_set_custom_action_enabled(params, v):
    vkeyName = multiget_deskkeys_vkeys_extract(params[0])
    __get_customactdata(__get_vkey(vkeyName)).setEnabled(v.v)

def multiple_deskkeys_vkeys_get_custom_action_enabled(params):
    vkeyName = multiget_deskkeys_vkeys_extract(params[0])
    return __get_customactdata(__get_vkey(vkeyName)).isEnabled()