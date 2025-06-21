class DeviceInfo(object):
    def __init__(self, ringnum, keynum, pentype, trackpad=None, control=None, key_direction=None):
        self.ringnum = ringnum
        self.keynum = keynum
        self.pentype = pentype
        self.trackpad = trackpad
        self.control = control
        self.key_direction = key_direction