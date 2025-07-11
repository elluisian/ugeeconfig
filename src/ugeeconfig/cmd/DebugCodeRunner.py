# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.


import sys

from .Value import *
from ..xml.ActionElement import *


DEBUG_FUNCTS = []


def debugStart():
    print("HELLO DEBUGGING")

def debugEnd():
    print("BYE DEBUGGING")


def valueTokenizerTest():
    lk = " ".join(sys.argv[1:])
    tokz = ValueTokenizer(lk)
    tk = tokz.nextToken()

    while not tk.isTokenType(TOKEN_EOI):
        print(tk)
        tk = tokz.nextToken()



def valueParserTest():
    lk = " ".join(sys.argv[1:])
    print(lk)
    pars = ValueParser(lk)
    els = pars.parse()
    for i in els:
        print(i)



def valueInstanceTest():
    v = Value("t")
    print("type is: " + v.getType())
    print(v)
    #v = Value("true")
    #print("type is: " + v.getType())
    #print(v)



def customActionParserTest():
    lk = str(sys.argv[1])
    v = Value(lk)

    #print(v)
    #print(type(v))
    #print(type(v.v))

    print(ActionElement._writeKeystrokesDebug(v.v.getKeystrokes()))





DEBUG_FUNCTS.append(debugStart)
DEBUG_FUNCTS.append(customActionParserTest)
#DEBUG_FUNCTS.append(valueTokenizerTest)
#DEBUG_FUNCTS.append(valueParserTest)
#DEBUG_FUNCTS.append(valueInstanceTest)
DEBUG_FUNCTS.append(debugEnd)