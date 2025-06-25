#!/bin/bash

# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



../ugeeconfig.sh from default-config.xml to gimp-config-ue16.xml set \
\
ue16.pen.button2.action_default 'mousek_sclick' \
\
ue16.tablet.key1.action_custom.label 'Paintbrush' \
ue16.tablet.key1.action_custom.action 'keys(p)' \
ue16.tablet.key1.action_custom.enabled 'true' \
\
ue16.tablet.key2.action_custom.label 'Pencil' \
ue16.tablet.key2.action_custom.action 'keys(n)' \
ue16.tablet.key2.action_custom.enabled 'true' \
\
ue16.tablet.key3.action_custom.label 'Lower zoom' \
ue16.tablet.key3.action_custom.action 'keys(minus)' \
ue16.tablet.key3.action_custom.enabled 'true' \
\
ue16.tablet.key4.action_custom.label 'Increase zoom' \
ue16.tablet.key4.action_custom.action 'keys(plus)' \
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
ue16.tablet.key7.action_custom.label 'Move objects' \
ue16.tablet.key7.action_custom.action 'keys(m)' \
ue16.tablet.key7.action_custom.enabled 'true' \
\
ue16.tablet.key8.action_custom.label 'Rectangular selection' \
ue16.tablet.key8.action_custom.action 'keys(r)' \
ue16.tablet.key8.action_custom.enabled 'true' \
\
ue16.tablet.key9.action_custom.label 'Eraser' \
ue16.tablet.key9.action_custom.action 'keys(shift+e)' \
ue16.tablet.key9.action_custom.enabled 'true' \
\
ue16.tablet.r.selected_wheel 1 \
\
ue16.tablet.r.wheel_movement1.usage 'usg_custom' \
ue16.tablet.r.wheel_movement1.label 'Increase/decrease brush size' \
ue16.tablet.r.wheel_movement1.ccw_label 'Decrease' \
ue16.tablet.r.wheel_movement1.cw_label 'Increase' \
ue16.tablet.r.wheel_movement1.ccw_action 'keys(altgr+egrave)' \
ue16.tablet.r.wheel_movement1.cw_action 'keys(altgr+plus)'
