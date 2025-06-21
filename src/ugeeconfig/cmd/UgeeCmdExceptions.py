class UgeeCmdParserException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UgeeCmdParserEOIException(Exception):
    def __init__(self):
        super().__init__()


class UgeeCmdParserHelpInvokedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UgeeCmdExecutorException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UgeeCmdExecutorNotALeafPropException(UgeeCmdExecutorException):
    def __init__(self, message):
        super().__init__(message)

class UgeeCmdExecutorNonExistentPropException(UgeeCmdExecutorException):
    def __init__(self, message):
        super().__init__(message)

class UgeeCmdExecutorIncompatibleValueTypeException(UgeeCmdExecutorException):
    def __init__(self, message):
        super().__init__(message)