PARSCMD_FROM = "from"
PARSCMD_TO = "to"
PARSOP_SET = "set"
PARSOP_GET = "get"
PARSOP_DOC = "doc"


import os
import sys


from ..utils.Object import *
from .UgeeCmdExceptions import *




class UgeeCmdParser(object):
    def __init__(self):
        self.args = list(map(lambda x : x.lower(), sys.argv[1:]))
        self.argc = len(self.args)
        self.idx = 0



    @staticmethod
    def showHelp():
        raise UgeeCmdParserHelpInvokedException(UgeeCmdParser.getHelp())



    @staticmethod
    def getHelp():
        return """ugeeconfig [from <filepath>] [(get|doc) <prop>+]
ugeeconfig [from <filepath>] [to <filepath>] set (<prop> <value)+

- if "from" is empty, then it generates a new file starting from the default configs;
- if "to" is empty, then everything is outputted to stdout, otherwise to file;
- Use the "doc" operation for getting more documentation on the single props;"""



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


        return operation




    def parse(self):
        operation = UgeeCmdParser.__createOperationObject()

        if self.argc == 0:
            UgeeCmdParser.showHelp()


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


        # Show minimal help, if no operation is requested
        if (operation.set == 0 and operation.get == 0 and operation.doc == 0):
            UgeeCmdParser.showMinimalHelp()


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
        return token in (PARSCMD_FROM, PARSCMD_TO,)




    @staticmethod
    def isOperator(token):
        return token in (PARSOP_SET, PARSOP_GET, PARSOP_DOC,)




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

            operation.props = list(operands)

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

        if requestedOps > 1:
            raise UgeeCmdParserException("Error: only one operator at a time can be used!")
