#!/bin/bash

# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



SCRIPT_DIR="$(dirname $(realpath ${BASH_SOURCE[0]}))"
SRC_DIR="$SCRIPT_DIR"/src
UGEECONFIG_SCRIPT="$SRC_DIR"/entrypoint.py

#echo "$SRC_DIR"
#echo "$PYTHONPATH"
PYTHONPATH="$PYTHONPATH:$SRC_DIR" python3 -B "$UGEECONFIG_SCRIPT" "$@"