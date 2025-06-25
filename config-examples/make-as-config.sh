#!/bin/bash

# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



if [ "$#" -eq 1 ]
then
    if [ -f "$1" ]
    then
        cp "$1" /usr/lib/ugeeTablet/conf/Ugee_Tablet.xml
    else
        echo "File \"$1\" is not a file!"
    fi
fi