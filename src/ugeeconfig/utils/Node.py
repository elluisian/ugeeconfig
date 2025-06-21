class Node(object):
    def __init__(self, parent=None):
        self.__children = []
        self.__childrenSz = 0
        self.__parent = parent


    def addChild(self, child):
        self.__children.append(child)
        self.__childrenSz += 1

    def getChild(self, ith):
        if 0 <= ith <= self.__childrenSz - 1:
            return self.__children[ith]
        return None

    def removeChild(self, ith):
        c = None
        if 0 <= ith <= self.__childrenSz - 1:
            c = self.__children[ith]
            del self.__children[ith]
        return c

    def getChildren(self):
        return list(self.__children)

    def getNoChildren(self):
        return self.__childrenSz

    def hasChildren(self):
        return self.getNoChildren() > 0

    def getParent(self):
        return self.__parent


    def previsit(self):
        stk = Stack()
        stk.push(self)

        available = []
        while not stk.isEmpty():
            el = stk.pop()

            print("ENCOUNTERED: " + str(el))

            if el.hasChildren():
                print("HAS CHILDREN, DESCENDING")
                children = reversed(el.getChildren())
                for i in children:
                    stk.push(i)
            else:
                print("HAS NO CHILDREN, ASCENDING")

            available.append((el, el.getParent(),))

        return available