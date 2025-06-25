# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



import sys

from .XMLElement import *




class InvalidXMLDataType(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidXMLTag(Exception):
    def __init__(self, message):
        super().__init__(message)





def bool_to_xmbool(v):
    return "1" if v else "0"

def float_to_xmfloat(v):
    return str(v)

def xmbool_to_bool(v):
    if v == "1":
        return True

    elif v == "0":
        return False

    raise InvalidXMLDataType("Passed data \"%s\" is not a valid xml bool!" % (v,))

def xmfloat_to_float(v):
    return float(v)

def xmint_to_int(v):
    return int(v)

def int_to_xmint(v):
    return str(v)


def get_children(el):
    return list(el)



def str_equals_insensitive(st1, st2):
    st1 = str(st1)
    st2 = str(st2)
    st1 = st1.lower()
    st2 = st2.lower()
    return st1 == st2



def str_startswith_insensitive(st1, st2):
    st1 = str(st1)
    st2 = str(st2)
    st1 = st1.lower()
    st2 = st2.lower()
    return st1.startswith(st2)




def printf(message, onStderr=False):
    if onStderr:
        sys.stderr.write(message)
    else:
        sys.stdout.write(message)