from .Action import *



class Actionable(ABC):
    def __init__(self, tagNo, actionData):
        self.tagNo = tagNo
        self.actionData = actionData

    def getTagNo(self):
        return self.tagNo

    def getCustomActionData(self):
        return self.actionData


class ActionableButton(Actionable):
    def __init__(self, tagNo, actid):
        super().__init__(tagNo, CustomActionData())
        self.actid = actid

    def getActid(self):
        return self.actid

    def setActid(self, actid):
        self.actid = actid


class ActionableWheelMovement(Actionable):
    def __init__(self, tagNo):
        super().__init__(tagNo, WheelCustomActionData())




class VirtualKey(ActionableButton):
    def __init__(self, tagno, actid):
        super().__init__(tagno, actid)

class TabletButton(ActionableButton):
    def __init__(self, tagno, actid, motid=None, show=True):
        super().__init__(tagno, actid)
        self.motid = motid
        self.show = show

    def getMotid(self):
        return self.motid

    def getShow(self):
        return self.show

class PenButton(ActionableButton):
    def __init__(self, tagno, actid):
        super().__init__(tagno, actid)

class WheelActMovement(ActionableWheelMovement):
    def __init__(self, tagno):
        super().__init__(tagno)