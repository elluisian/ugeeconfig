from .Button import VirtualKey



class DesktopShortcutKeys(object):
    def __init__(self):
        self.win_fixed = False
        self.zoom = 1.0 # Zoom
        self.displayed_at_cursor = True
        self.row_no = 0
        self.col_no = 0
        self.vkeys = ()


    @staticmethod
    def makeDefault(win_fixed, zoom, displayedAtCursor, row_no, col_no, vkeys):
        dsk = DesktopShortcutKeys()
        dsk.win_fixed = win_fixed
        dsk.zoom = zoom
        dsk.displayedAtCursor = displayedAtCursor
        dsk.row_no = row_no
        dsk.col_no = col_no
        dsk.vkeys = tuple(vkeys)
        return dsk



    def getVKeyByTagNo(self, tagno):
        for i in self.vkeys:
            if i.tagNo == tagno:
                return i

        return None



    def getVKeysNames(self):
        vkk = []
        for i in self.vkeys:
            vkk.append(i.tagNo)
        return vkk