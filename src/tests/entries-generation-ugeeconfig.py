# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.


from copy import deepcopy
import sys


class Object(object):
    def __init__(self, attrs={}):
        for i in attrs.keys():
            setattr(self, i, attrs[i])



class Stack(object):
    def __init__(self):
        self.__data = []
        self.__dataSz = 0

    def push(self, datum):
        self.__data.append(datum)
        self.__dataSz += 1


    def top(self):
        if self.isEmpty():
            return None

        return self.__data[self.__dataSz - 1]

    def pop(self):
        t = self.top()
        if t is not None:
            del self.__data[self.__dataSz - 1]
            self.__dataSz -= 1
        return t

    def size(self):
        return self.__dataSz

    def isEmpty(self):
        return self.size() == 0

    def __deepcopy__(self, memo):
        stk = Stack()
        stk.__data = list(self.__data)
        stk.__dataSz = self.__dataSz
        return stk

    def __repr__(self):
        msg = "STK<"

        for idx, datum in enumerate(self.__data):
            if datum is None:
                msg += "NONE"
            else:
                msg += str(datum)

            if idx < self.__dataSz - 1:
                msg += ","

        msg += ">"
        return msg

    def __str__(self):
        return self.__repr__()


    def clear(self):
        self.__data.clear()
        self.__dataSz = 0




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



NODET_ROOT = -1
NODET_MULTI = 0
NODET_SINGLE = 1
NODET_LEAF = 2


class Prop(Node):
    HIERARCHY = None
    HIERARCHY_GRAMMAR = None

    def __init__(self, name, nodeType, multiget, parent=None):
        super().__init__(parent)
        self.__name = name
        self.__multiget = multiget
        self.__nodeType = nodeType


    @staticmethod
    def makeRoot():
        return Prop("", NODET_ROOT, None, None)

    @staticmethod
    def makeSingle(name, parent):
        return Prop(name, NODET_SINGLE, None, parent)

    @staticmethod
    def makeMulti(name, multiget, parent):
        return Prop(name, NODET_MULTI, multiget, parent)

    @staticmethod
    def makeLeaf(name, parent):
        return Prop(name, NODET_LEAF, None, parent)

    def isSingle(self):
        return self.__nodeType == NODET_SINGLE

    def isLeaf(self):
        return self.__nodeType == NODET_LEAF

    def isMulti(self):
        return self.__nodeType == NODET_MULTI

    def isRoot(self):
        return self.__nodeType == NODET_ROOT

    def getMultiget(self):
        return self.__multiget

    def addSingles(self, *singles):
        for i in singles:
            name, = i
            p = Prop.makeSingle(name, self)
            self.addChild(p)
            setattr(self, name, p)

    def addMultis(self, *multis):
        for i in multis:
            name, multiget = i
            p = Prop.makeMulti(name, multiget, self)
            self.addChild(p)
            setattr(self, name, p)

    def addLeaves(self, *leaves):
        for i in leaves:
            name, = i
            p = Prop.makeLeaf(name, self)
            self.addChild(p)
            setattr(self, name, p)

    def getName(self):
        return self.__name

    def getChildByName(self, name):
        for i in self.getChildren():
            if i.getName() == name:
                return i
        return None


    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.isRoot():
            return ""
        elif self.getParent().isRoot():
            return "%s" % (self.getName(),)
        else:
            return "%s->%s" % (self.getParent(), self.getName())



    @staticmethod
    def visit():
        latest = Prop.HIERARCHY
        st = Stack()
        st.push(latest)
        available = []

        while not st.isEmpty():
            p = st.pop()

            if p.hasChildren():
                ll = list(reversed(p.getChildren()))
                for i in ll:
                    st.push(i)
            else:
                available.append(p)

        return available



    @staticmethod
    def searchPropByPath(proppath):
        compnames = proppath.split(".")

        i = len(compnames) - 1
        while i >= 0:
            if compnames[i] == "":
                del compnames[i]
            i -= 1

        latest = Prop.HIERARCHY
        nonExistentTerritory = False
        nonExistents = []

        for i in compnames:
            if not nonExistentTerritory:
                child = latest.getChildByName(i)
                if child is not None:
                    latest = child
                else:
                    nonExistents.append(i)
                    nonExistentTerritory = True
            else:
                nonExistents.append(i)

        return (latest, nonExistents,)




    @staticmethod
    def generateHierarchyFromGrammar():
        if Prop.HIERARCHY is None:
            navStk = Stack()
            navStk.push(Prop.HIERARCHY_GRAMMAR)

            navChRemStk = Stack()
            navChRemStk.push(1)

            params = []

            creatRoot = Prop.makeRoot()
            Prop.HIERARCHY = creatRoot
            creatLatest = creatRoot

            creatStk = Stack()
            creatStk.push((creatLatest, list(params), navStk, deepcopy(navChRemStk)))


            while not creatStk.isEmpty():
                latest = creatStk.pop()
                creatLatest, params, navStk, navChRemStk = latest

                print("Restoring " + str(navStk))

                while not navStk.isEmpty():
                    print(navStk)
                    navEl = navStk.pop()
                    print(navEl)

                    # Update the list of available children, after extracting this one
                    remaining = navChRemStk.pop()

                    # Remove one from the remaining children, as the most recent one was popped
                    remaining -= 1
                    navChRemStk.push(remaining)


                    # Add children only if not Multi, otherwise, handle specially
                    if navEl.hasChildren() and not navEl.isMulti():
                        print("I HAVE CHILDREN:")

                        # Save the newest available children (number of them)
                        noChildren = navEl.getNoChildren()
                        navChRemStk.push(noChildren)

                        # Push the actual children
                        children = list(reversed(navEl.getChildren()))
                        for i in children:
                            navStk.push(i)

                        #print("CHILDREN ADDED TO STACK")


                    if navEl.isMulti():
                        print("I AM MULTI: %s, %s" % (str(navEl), str(params)))

                        # Preserve current analysis, we'll go back to it later
                        preserveLatest = creatLatest
                        if remaining == 0:
                            # If this is the last of his siblings (=the last of his parent's children), we want to go upward BEFORE preserving, in order to properly construct the following remaining nodes
                            navChRemStk.pop()
                            preserveLatest = creatLatest.getParent()


                        print("Preserving current stack: " + str(navStk) + "; " + str(preserveLatest))
                        creatStk.push((
                            preserveLatest,
                            list(params),
                            deepcopy(navStk),
                            deepcopy(navChRemStk),
                        ))

                        navStk.clear()
                        children = list(reversed(navEl.getChildren()))
                        for i in children:
                            navStk.push(i)

                        navChRemStk.clear()
                        noChildren = navEl.getNoChildren()
                        navChRemStk.push(noChildren)


                        multiget = navEl.getMultiget()
                        multiNames = multiget(params)

                        for i in multiNames:
                            currParams = list(params)
                            currParams.append(i)
                            print("Saving " + str(navStk) + " for " + i)
                            p = Prop.makeSingle(i, creatLatest)
                            creatStk.push((
                                p,
                                currParams,
                                deepcopy(navStk),
                                deepcopy(navChRemStk)
                            ))
                            creatLatest.addChild(p)

                        break

                    elif navEl.isSingle():
                        print("I AM SINGLE: " + str(navEl) + ", " + str(params))
                        p = Prop.makeSingle(navEl.getName(), creatLatest)
                        creatLatest.addChild(p)
                        creatLatest = p

                    elif navEl.isLeaf():
                        print("I AM LEAF: " + str(navEl) + ", " + str(params))
                        print("creatLatest: " + str(creatLatest))
                        p = Prop.makeLeaf(navEl.getName(), creatLatest)
                        creatLatest.addChild(p)

                        nUpwards = 0

                        # Count how many times the hierarchy must go up (within parent in parent)
                        while remaining == 0 and not navChRemStk.isEmpty():
                            remaining = navChRemStk.pop()
                            nUpwards += 1

                        # Restore the last available children (popped earlier, the first non-zero one)
                        # Remember the depth of the tree goes from 0 to navChRemStk.size() - 1
                        navChRemStk.push(remaining)

                        # Finally, move up in the hierarchy in the "construction node", so that future nodes, are correctly created at the right places
                        for i in range(0, nUpwards - 1):
                            creatLatest = creatLatest.getParent()

                        print("KLCreateLatest: " + str(creatLatest))

                    else:
                        pass
                        #print("NO RECOGNIZED")


                    #print(navStk)




"""
DEV (MULTI)
    A (SINGLE)
        B (SINGLE)
            C (LEAF)
        H (SINGLE)
            I (LEAF)
        J (LEAF)
        K (LEAF)
        L (LEAF)
    D (MULTI)
        F (LEAF)
    E (MULTI)
        G (LEAF)
"""


def multiget_dev(params):
    return ("DEVGATTO", "DEVCANE", "DEVPOLLO")


def multiget_d(params):
    dev = params[0]

    if dev == "DEVGATTO":
        return ("DMAO", "DMIAO", "DPURRR",)
    elif dev == "DEVCANE":
        return ("DWOF", "DAUUUU",)
    elif dev == "DEVPOLLO":
        return ("DCOCOCO",)

    return None



def multiget_e(params):
    dev = params[0]

    if dev == "DEVGATTO":
        return ("EGRAFFIO",)
    elif dev == "DEVCANE":
        return ("EFEDELE", "ECORAGGIOSO",)
    elif dev == "DEVPOLLO":
        return ("EPOTENTE", "EPROTETTIVO", "ECHIASSOSO",)

    return None




if Prop.HIERARCHY_GRAMMAR is None:
    Prop.HIERARCHY_GRAMMAR = Prop.makeRoot()
    Prop.HIERARCHY_GRAMMAR.addMultis(("DEV", multiget_dev,))
    Prop.HIERARCHY_GRAMMAR.DEV.addSingles(("A",))
    Prop.HIERARCHY_GRAMMAR.DEV.A.addSingles(("B",),)
    Prop.HIERARCHY_GRAMMAR.DEV.A.B.addLeaves(("C",), ("J",))
    Prop.HIERARCHY_GRAMMAR.DEV.addMultis(("D", multiget_d,),
        ("E", multiget_e,))
    Prop.HIERARCHY_GRAMMAR.DEV.D.addLeaves(("F",))
    Prop.HIERARCHY_GRAMMAR.DEV.E.addLeaves(("G",))


Prop.generateHierarchyFromGrammar()


#k = Prop.searchPropByPath("CANE.WOF.E")
#print(k)

lll = Prop.visit()
for i in lll:
    print(i)