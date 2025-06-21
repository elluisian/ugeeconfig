from ...utils.lexer.CommonTokenReaders import *
from ...utils.lexer.NumericTokReader import *
from ...utils.lexer.Tokenizer import *

"""
KEYS(ctrl+alt+p,ctrl+test+t) # TYPE 1
MOUSE(ctrl+leftclick,alt+rightclick) # TYPE 2
FUNCT(<name>) # TYPE 3
EXEC(name, path) # TYPE 5
SYSOP(<name>) # TYPE 6
MULTIM(<name>) # TYPE 7
NOP() # TYPE 10
UNSET() # remove what was set
"""


# Data types
TOKEN_TRUE = "tk_true"
TOKEN_FALSE = "tk_false"
TOKEN_RECTANGLE = "tk_rectangle"
TOKEN_PRESSURE = "tk_pressure"


# Custom actions
TOKEN_KEYS = "tk_keys"
TOKEN_MOUSE = "tk_mouse"
TOKEN_FUNCT = "tk_funct"
TOKEN_EXEC = "tk_exec"
TOKEN_SYSOP = "tk_sysop"
TOKEN_MULTIMEDIA = "tk_multimedia"
TOKEN_NOP = "tk_nop"
TOKEN_UNSET = "tk_unset"


TOKEN_ARG_SEP = "tk_arg_sep"
TOKEN_ARG_GOPEN = "tk_arg_gopen"
TOKEN_ARG_GCLOSE = "tk_arg_gclose"
TOKEN_ARG_PLUS = "tk_arg_plus"





class ValueTokenizer(Tokenizer):
    def __init__(self, inp):
        super().__init__(inp, ",+() ")

    def getTokenReaders(self, inpr, disruptingAlphabet):
        return (
            SpaceTokReader(inpr),
            IdentifierKeywordTokReader.make(inpr, disruptingAlphabet,
                ("t", TOKEN_TRUE, True,),
                ("true", TOKEN_TRUE, True,),
                ("f", TOKEN_FALSE, True,),
                ("false", TOKEN_FALSE, True,),
                ("rect", TOKEN_RECTANGLE, True,),
                ("press", TOKEN_PRESSURE, True,),
                ("keys", TOKEN_KEYS, True,),
                ("mouse", TOKEN_MOUSE, True,),
                ("funct", TOKEN_FUNCT, True,),
                ("exec", TOKEN_EXEC, True,),
                ("sysop", TOKEN_SYSOP, True,),
                ("multim", TOKEN_MULTIMEDIA, True,),
                ("nop", TOKEN_NOP, True,),
                ("unset", TOKEN_UNSET, True,),
            ),
            FloatTokReader(inpr),
            NumericTokReader(inpr),
            OperatorTokReader.make(inpr, ",", TOKEN_ARG_SEP),
            OperatorTokReader.make(inpr, "(", TOKEN_ARG_GOPEN),
            OperatorTokReader.make(inpr, ")", TOKEN_ARG_GCLOSE),
            OperatorTokReader.make(inpr, "+", TOKEN_ARG_PLUS),
        )