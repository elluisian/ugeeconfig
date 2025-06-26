# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



from .Action import *



class Actionable(ABC):
    def __init__(self, tagNo, actionData):
        self.tagNo = tagNo
        self.actionData = actionData

    def getTagNo(self):
        return self.tagNo

    def getCustomActionData(self):
        return self.actionData

    @abstractmethod
    def __deepcopy__(self, m):
        pass


class ActionableButton(Actionable):
    def __init__(self, tagNo, actid):
        super().__init__(tagNo, CustomActionData())
        self.actid = actid

    def getActid(self):
        return self.actid

    def setActid(self, actid):
        self.actid = actid

    @abstractmethod
    def __deepcopy__(self, m):
        pass


class ActionableWheelMovement(Actionable):
    def __init__(self, tagNo):
        super().__init__(tagNo, WheelCustomActionData())

    @abstractmethod
    def __deepcopy__(self, m):
        pass




class VirtualKey(ActionableButton):
    def __init__(self, tagno, actid):
        super().__init__(tagno, actid)

    def __deepcopy__(self, m):
        return VirtualKey(self.tagNo, self.actid)




class TabletButton(ActionableButton):
    def __init__(self, tagno, actid, motid=None, show=True):
        super().__init__(tagno, actid)
        self.motid = motid
        self.show = show

    def getMotid(self):
        return self.motid

    def getShow(self):
        return self.show

    def __deepcopy__(self, m):
        return TabletButton(self.tagNo, self.actid, self.motid, self.show)




class PenButton(ActionableButton):
    def __init__(self, tagno, actid):
        super().__init__(tagno, actid)

    def __deepcopy__(self, m):
        return PenButton(self.tagNo, self.actid)




class WheelActMovement(ActionableWheelMovement):
    def __init__(self, tagno):
        super().__init__(tagno)

    def __deepcopy__(self, m):
        return WheelActMovement(self.tagNo)