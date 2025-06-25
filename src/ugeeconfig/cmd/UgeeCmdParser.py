PARSCMD_FROM = "from"
PARSCMD_TO = "to"
PARSOP_SET = "set"
PARSOP_GET = "get"
PARSOP_DOC = "doc"
PARSOP_ACTIDS = "actids"
PARSOP_XKEYSYMS = "xkeysyms"



import os
import sys


from ..utils.Object import *
from ..utils.utils import str_equals_insensitive
from .UgeeCmdExceptions import *




class UgeeCmdParser(object):
    def __init__(self):
        self.args = list(sys.argv[1:])
        self.argc = len(self.args)
        self.idx = 0



    @staticmethod
    def showHelp():
        raise UgeeCmdParserHelpInvokedException(UgeeCmdParser.getHelp())



    @staticmethod
    def getHelp():
        return """ugeeconfig [from <filepath>] [(get|doc) <prop>*]
ugeeconfig [from <filepath>] [to <filepath>] set (<prop> <value)+
ugeeconfig [to <filepath>]
ugeeconfig actids (keys|mouse|funct|sysop|multimedia|all)*
ugeeconfig xkeysyms

- Use the "get" operator to get prop values;
- Use the "doc" operator to get more documentation on single props;
- Use the "set" operator to set prop values;
- Use the "to" command without any operator to generate a default config file;
- Use the "actids" operation to get a list of the available actids;
- Use the "xkeysyms" operation to show all the XKeysyms names;
- if "from" is omitted, then the default configuration will be used as base;
- if "to" is omitted, then everything is outputted to stdout, otherwise to file;



- <filepath>: a simple file path;
- <prop>: is a dot-separated path, use the 'doc' operator to know the available ones;
- <value>: may be:
    - a string;
    - an integer with one of the following forms:
        - 0b-prefixed binary integer (e.g. 0b101010);
        - b-suffixed binary integer (e.g. 1010101010b);
        - 0-prefixed octal integer (e.g. 023);
        - 0o-prefixed octal integer (e.g. 0o23);
        - o-suffixed octal integer (e.g. 234o);
        - 0d-prefixed decimal integer (e.g. 0d123499);
        - d-suffixed decimal integer (e.g. 123894d);
        - 0x-prefixed hexadecimal integer (e.g. 0xaf98d);
        - 0h-prefixed hexadecimal integer (e.g. 0haf98d);
        - x-suffixed hexadecimal integer (e.g. af98dx);
        - h suffixed hexadecimal integer (e.g. af98dh);
    - a float of the form "(decimal digit)*.(decimal digit)+";
    - a rectangle of the form "rect(x, y, w, h)", with "x", "y", "w", and "h" being integers;
    - a "pressurepoints" of the form "press(p0, p1x, p1y, p2)", with "p0" and "p2" being integers, representing, respectively, the x-axes of the first and final points of the pressure, while "p1x" and "p1y" are an xy-coordinate for the middle point;
    - an actid (integer and/or symbolic actid name);
    - a wheel usage (symbolic name), with the values "usg_default", "usg_custom", "usg_nop";
    - a custom action with one of the following forms:
        - "keys(<keystroke>[,<keystroke>]*)" where <keystroke> is of the form (<keysym>[+<keysym>]*), basically, a bunch of lists of keysyms separated by pluses, separated by commas;
        - "mouse(<mouseactid>[+<mouseactid>]*)" where <mouseactid> is a mouse actid;
        - "exec(<execpath>)" where <execpath> is a path to an executable to be run (command line parameters are not supported)
        - "funct(<functactid>)" where <functactid> is a function actid;
        - "sysop(<sysopactid>)" where <sysopactid> is a sysop actid;
        - "multim(<multimactid>)" where <multimactid> is a multimedia actid;


NOTE: The current locale AFFECTS the needed xkeysyms to perform an action, in general, you want to consider the actual keys you press in order to produce a certain output instead of the output itself.
For example, in Italian keyboards, in order to output the left bracket, you need to press AltGr and the grave accented e keys.
If using an Italian locale, 'keys(bracketleft)' doesn't work, but 'keys(altgr+egrave)' does. For the same reason, `keys(bracketleft)` will correctly work on US locales.
Other than using the "xkeysyms" operator, you can use utilities like xev, to correctly get the actual xkeysyms for the single keys of the keyboard.

NOTE 2: Utilities like ibus still AFFECT the locale.
"""



    @staticmethod
    def __createOperationObject():
        operation = Object()

        operation.fromP = Object()
        operation.fromP.count = 0
        operation.fromP.value = None

        operation.toP = Object()
        operation.toP.count = 0
        operation.toP.value = None

        operation.props = []
        operation.values = []
        operation.set = 0
        operation.get = 0
        operation.doc = 0
        operation.actids = 0
        operation.xkeysyms = 0


        return operation




    def parse(self):
        operation = UgeeCmdParser.__createOperationObject()

        eoiReached = False
        while not eoiReached:
            try:
                token = self.__nextToken()
                if UgeeCmdParser.isCommand(token):
                    self.__handleCommandToken(token, operation)

                elif UgeeCmdParser.isOperator(token):
                    eoiReached = self.__handleOperatorToken(token, operation)

                else:
                    raise UgeeCmdParserException("Error: Unknown token type \"%s\"" % (token,))

            except UgeeCmdParserEOIException as ex:
                eoiReached = True


        # Handle some of the errors
        UgeeCmdParser.__handleErrorsOfMultipleUsages(operation)


        # Show help, if no operation is requested
        if operation.set == 0 and operation.get == 0 and operation.doc == 0 and operation.actids == 0 and operation.xkeysyms == 0:
            if (operation.toP.count == 0 and operation.fromP.count == 0) or\
                (operation.toP.count > 0 and operation.fromP.count > 0):
                UgeeCmdParser.showHelp()
            # if no fromP and a toP is set, then consider this a valid operation, as it's as if the generation of the default config file is requested.

        return operation




    def __nextToken(self):
        if self.idx < self.argc:
            el = self.args[self.idx]
            self.idx += 1
        else:
            raise UgeeCmdParserEOIException()

        return el




    def __putBackToken(self):
        if self.idx >= 0:
            self.idx -= 1




    @staticmethod
    def isCommand(token):
        return str_equals_insensitive(token, PARSCMD_FROM) or\
            str_equals_insensitive(token, PARSCMD_TO)




    @staticmethod
    def isOperator(token):
        return str_equals_insensitive(token, PARSOP_SET) or\
            str_equals_insensitive(token, PARSOP_GET) or\
            str_equals_insensitive(token, PARSOP_DOC) or\
            str_equals_insensitive(token, PARSOP_ACTIDS) or\
            str_equals_insensitive(token, PARSOP_XKEYSYMS)




    def __handleCommandToken(self, token, operation):
        if token == PARSCMD_FROM:
            operation.fromP.count += 1
            commsetting = self.__nextToken()
            if not os.path.isdir(commsetting) and not os.path.exists(commsetting):
                raise UgeeCmdParserException("Error: non-existing path \"%s\" specified to command \"%s\"" % (commsetting, token,))
            operation.fromP.value = commsetting


        elif token == PARSCMD_TO:
            operation.toP.count += 1
            commsetting = self.__nextToken()
            if os.path.isdir(commsetting):
                raise UgeeCmdParserException("Error: path \"%s\" specified to command \"%s\" is a directory" % (token, commsetting,))
            operation.toP.value = commsetting




    def __handleOperatorToken(self, token, operation):
        eoiReached, operands = self.__getAvailableOperands()

        operation.props = []
        operation.values = []

        if token == PARSOP_SET:
            operation.set += 1

            nOperands = len(operands)
            if nOperands % 2 != 0 or nOperands == 0:
                raise UgeeCmdParserException("Error: for \"set\" operator to be successful, an even number of operands must be present!")

            for i in range(0, nOperands, 2):
                p, v = operands[i:i + 2]
                operation.props.append(p)
                operation.values.append(v)


        else:
            if token == PARSOP_GET:
                operation.get += 1

            elif token == PARSOP_DOC:
                operation.doc += 1

            elif token == PARSOP_ACTIDS:
                operation.actids += 1

            elif token == PARSOP_XKEYSYMS:
                operation.xkeysyms += 1

            operation.props = list(operands)

            if len(operation.props) > 0 and token == PARSOP_XKEYSYMS:
                raise UgeeCmdParserException("Error: %s operator doesn't expect operands!" % (PARSOP_XKEYSYMS,))


        return eoiReached




    def __getAvailableOperands(self):
        # Handle all the given parameters
        noCommandAndOp = False
        operands = []
        eoiReached = False
        while not eoiReached and not noCommandAndOp: # check for EOI and commands/operations
            try:
                operand = self.__nextToken()
                if not UgeeCmdParser.isCommand(operand) and not UgeeCmdParser.isOperator(operand):
                    operands.append(operand)
                else:
                    self.__putBackToken()
                    noCommandAndOp = True

            except UgeeCmdParserEOIException as ex:
                eoiReached = True

        return (eoiReached, operands)



    @staticmethod
    def __handleErrorsOfMultipleUsages(operation):
        # Multiple usages of operators
        if operation.set > 1:
            raise UgeeCmdParserException("Error: multiple uses of the \"set\" operator!", (PARSOP_SET,))

        if operation.get > 1:
            raise UgeeCmdParserException("Error: multiple uses of the \"get\" operator!", (PARSOP_GET,))

        if operation.doc > 1:
            raise UgeeCmdParserException("Error: multiple uses of the \"%s\" operator!" % (PARSOP_DOC,))

        if operation.actids > 1:
            raise UgeeCmdParserException("Error: multiple uses of the \"%s\" operator!" % (PARSOP_ACTIDS,))

        if operation.xkeysyms > 1:
            raise UgeeCmdParserException("Error: multiple uses of the \"%s\" operator!" % (PARSOP_XKEYSYMS,))


        # Multiple usages of commands
        if operation.fromP.count > 1:
            raise UgeeCmdParserException("Error: multiple uses of the \"%s\" command!" % (PARSCMD_FROM,))

        if operation.toP.count > 1:
            raise UgeeCmdParserException("Error: multiple uses of the \"%s\" command!" % (PARSCMD_TO,))


        # Multiple requested operators
        requestedOps = 0
        if operation.set > 0:
            requestedOps += 1

        if operation.get > 0:
            requestedOps += 1

        if operation.doc > 0:
            requestedOps += 1

        if operation.actids > 0:
            requestedOps += 1

        if operation.xkeysyms > 0:
            requestedOps += 1

        if requestedOps > 1:
            raise UgeeCmdParserException("Error: only one operator at a time can be used!")
