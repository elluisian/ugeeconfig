class Ring(object):
    def __init__(self, tag_name, selected_wheel, mode=None, wheel_actmovements=[]):
        self.tag_name = tag_name
        self.selected_wheel = selected_wheel
        self.mode = mode
        self.wheel_actmovements = wheel_actmovements



    def getWheelActMovements(self):
        return list(self.wheel_actmovements)


    def getWheelActMovementByTagNo(self, tagno):
        for i in self.wheel_actmovements:
            if tagno == i.tagNo:
                return i
        return None


    def getWheelActMovementNames(self):
        whmov = []
        for i in self.wheel_actmovements:
            whmov.append(i.tagNo)

        return whmov