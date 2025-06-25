# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.


class ValueParserException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValueUnsupportedXKeysymException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValueInvalidActidException(Exception):
    def __init__(self, message):
        super().__init__(message)