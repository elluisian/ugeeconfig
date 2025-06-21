class Object(object):
    def __init__(self, ds={}):
        keys = ds.keys()
        for i in keys:
            v = ds[i]
            setattr(self, i, v)

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return self.__str__()