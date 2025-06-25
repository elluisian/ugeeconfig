#!/bin/bash

# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



../ugeeconfig.sh from default-config.xml to xournalpp-config-ue16.xml set \
\
ue16.pen.button2.action_default 'mousek_sclick' \
\
ue16.tablet.key1.action_custom.label 'Pen' \
ue16.tablet.key1.action_custom.action 'keys(shift+ctrl+p)' \
ue16.tablet.key1.action_custom.enabled 'true' \
\
ue16.tablet.key2.action_custom.label 'Highlighter' \
ue16.tablet.key2.action_custom.action 'keys(shift+ctrl+h)' \
ue16.tablet.key2.action_custom.enabled 'true' \
\
ue16.tablet.key3.action_custom.label 'Eraser' \
ue16.tablet.key3.action_custom.action 'keys(shift+ctrl+e)' \
ue16.tablet.key3.action_custom.enabled 'true' \
\
ue16.tablet.key4.action_custom.label 'Text' \
ue16.tablet.key4.action_custom.action 'keys(shift+ctrl+t)' \
ue16.tablet.key4.action_custom.enabled 'true' \
\
ue16.tablet.key5.action_custom.label 'Copy' \
ue16.tablet.key5.action_custom.action 'keys(ctrl+c)' \
ue16.tablet.key5.action_custom.enabled 'true' \
\
ue16.tablet.key6.action_custom.label 'Paste' \
ue16.tablet.key6.action_custom.action 'keys(ctrl+v)' \
ue16.tablet.key6.action_custom.enabled 'true' \
\
ue16.tablet.key7.action_custom.label 'Delete' \
ue16.tablet.key7.action_custom.action 'keys(delete)' \
ue16.tablet.key7.action_custom.enabled 'true' \
\
ue16.tablet.key8.action_custom.label 'Rectangular selection' \
ue16.tablet.key8.action_custom.action 'keys(shift+ctrl+r)' \
ue16.tablet.key8.action_custom.enabled 'true' \
\
ue16.tablet.key9.action_custom.label 'Hand' \
ue16.tablet.key9.action_custom.action 'keys(shift+ctrl+a)' \
ue16.tablet.key9.action_custom.enabled 'true' \
\
ue16.tablet.r.selected_wheel 1 \
\
ue16.tablet.r.wheel_movement1.usage 'usg_custom' \
ue16.tablet.r.wheel_movement1.label 'Increase/decrease zoom' \
ue16.tablet.r.wheel_movement1.ccw_label 'Decrease' \
ue16.tablet.r.wheel_movement1.cw_label 'Increase' \
ue16.tablet.r.wheel_movement1.ccw_action 'keys(ctrl+minus)' \
ue16.tablet.r.wheel_movement1.cw_action 'keys(ctrl+plus)'
