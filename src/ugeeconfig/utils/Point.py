class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __deepcopy__(self, m):
        return Point(self.x, self.y)