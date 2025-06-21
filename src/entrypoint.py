#!/usr/bin/python3

from ugeeconfig.cmd.UgeeCmdParser import *
from ugeeconfig.cmd.UgeeCmdExecutor import *

DEBUG_MODE = False
DEBUG_ONLY = True




if DEBUG_MODE:
    from ugeeconfig.cmd.DebugCodeRunner import DEBUG_FUNCTS
    for i in DEBUG_FUNCTS:
        i()

    if DEBUG_ONLY:
        exit(1)


cmdparser = UgeeCmdParser()
try:
    operation = cmdparser.parse()
    xx = UgeeCmdExecutor(operation)
    xx.execute()

except UgeeCmdParserException as ex1:
    print(ex1)

except UgeeCmdParserHelpInvokedException as ex2:
    print(ex2)

except UgeeCmdExecutorException as ex3:
    print(ex3)