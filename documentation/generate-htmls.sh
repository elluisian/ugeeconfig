#!/bin/bash

# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



AUTHOR="elluisian"
TEMPLATE_DOC="./output-document-template.html"

FILE_1="value-parser-tokenizer_documentation"
TITLE_1="Value parser documentation and numeric tokenizer"
FILE_2="xml-configfile_documentation"
TITLE_2="Ugee driver xml Configuration file documentation"


pandoc "$FILE_1".md -o "$FILE_1".html --template="$TEMPLATE_DOC" -M title="$TITLE_1" -M author="$AUTHOR"
pandoc "$FILE_2".md -o "$FILE_2".html --template="$TEMPLATE_DOC" -M title="$TITLE_2" -M author="$AUTHOR"