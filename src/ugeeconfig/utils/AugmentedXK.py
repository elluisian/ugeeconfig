#!/usr/bin/python3

# This module adds some supplementary functionalities to Xlib.XK (so the name).
# Inspired by pykey/critkey (https://shallowsky.com/blog/programming/crikey-python-and-xtest.html).
# To better use it, it should be sufficient to do: from AugmentedXK import Xlib

import Xlib.display
import Xlib.X
import Xlib.XK


from .utils import str_equals_insensitive


# This was almost blatantly copied from pykey.
# For some keysyms, it would be nice to have "friendlier" names, I guess.
Xlib.XK.Custom_XK_mapping = {
    'Newline' : "Return",  # For some reason this needs to be CR, not LF
    'Carriage' : "Return",
     '!' : "exclam",
     '#' : "numbersign",
     '%' : "percent",
     '$' : "dollar",
     '&' : "ampersand",
     '"' : "quotedbl",
    '\'' : "apostrophe",
     '(' : "parenleft",
     ')' : "parenright",
     '*' : "asterisk",
     '=' : "equal",
     '+' : "plus",
     ',' : "comma",
     '-' : "minus",
     '.' : "period",
     '/' : "slash",
     ':' : "colon",
     ';' : "semicolon",
     '<' : "less",
     '>' : "greater",
     '?' : "question",
     '@' : "at",
     '[' : "bracketleft",
     ']' : "bracketright",
    '\\' : "backslash",
     '^' : "asciicircum",
     '_' : "underscore",
     '`' : "grave",
     '{' : "braceleft",
     '|' : "bar",
     '}' : "braceright",
     '~' : "asciitilde",
   "ESC" : "Escape",
"Ctrl_L" : "Control_L",
"Ctrl_R" : "Control_R",
  "Ctrl" : "Control_L",
 "Shift" : "Shift_L",
 "AltGr" : "ISO_Level3_Shift",
   "Alt" : "Alt_L",
}
Xlib.XK.Augmented_XK_mapping = {
    "keynames": {},
    "keysyms": {}
}
Xlib.XK.displayinst = Xlib.display.Display()




def get_available_keynames():
    properties = list(dir(Xlib.XK))
    propertiesSz = len(properties)

    for i in reversed(range(0, propertiesSz)):
        if not properties[i].startswith("XK_"):
            del properties[i]
        else:
            properties[i] = properties[i][3:]

    return properties


def regenerate_augmented_xk_mapping():
    keynames = get_available_keynames()
    #print(keynames)
    for i in keynames:
        keysym = Xlib.XK.string_to_keysym(i)
        Xlib.XK.Augmented_XK_mapping["keynames"][i] = keysym
        Xlib.XK.Augmented_XK_mapping["keysyms"][keysym] = i





def solve_keyname(keyname):
    keyr = None

    for i in list(Xlib.XK.Custom_XK_mapping.keys()):
        if str_equals_insensitive(keyname, i):
            keyr = Xlib.XK.Custom_XK_mapping[i]

    for i in list(Xlib.XK.Augmented_XK_mapping["keynames"].keys()):
        if str_equals_insensitive(keyname, i):
            keyr = i

    return keyr





def get_keysym(keyname):
    keyname = solve_keyname(keyname)

    keyV = None
    if keyname is not None:
        keyV = Xlib.XK.Augmented_XK_mapping["keynames"][keyname]

    return keyV


def get_keyname(keysym):
    keyname = None

    if keysym in Xlib.XK.Augmented_XK_mapping["keysyms"]:
        keyname = Xlib.XK.Augmented_XK_mapping["keysyms"][keysym]

    return keyname


def get_keycode(keysym):
    return Xlib.XK.displayinst.keysym_to_keycode(keysym)


def get_keysym_keycode(ch):
    keysym = get_keysym(ch)
    if keysym is None:
        return None

    keycode = get_keycode(keysym)

    return (keysym, keycode,)


def get_available_augmented_keynames():
    ls =  list(Xlib.XK.Custom_XK_mapping.keys())
    ls.extend(list(Xlib.XK.Augmented_XK_mapping["keynames"].keys()))
    return ls









Xlib.XK.regenerated_augmented_xk_mapping = regenerate_augmented_xk_mapping
Xlib.XK.get_augmented_keysym = get_keysym
Xlib.XK.get_augmented_keyname = get_keyname
Xlib.XK.get_augmented_keycode = get_keycode
Xlib.XK.get_augmented_keysym_keycode = get_keysym_keycode
Xlib.XK.get_available_augmented_keynames = get_available_augmented_keynames



###############################
# Load various keysyms groups #
###############################
Xlib.XK.load_keysym_group("latin2")
Xlib.XK.load_keysym_group("xkb")

# Perform the generation of augmented xks
regenerate_augmented_xk_mapping()




# Test section
if __name__ == "__main__":
    p = Xlib.XK.get_available_augmented_keynames()
    l = len(p)
    print(Xlib.XK.get_augmented_keysym("ISO_Level3_Shift"))
    print(dir(Xlib.XK))
    print(Xlib.XK.Augmented_XK_mapping)