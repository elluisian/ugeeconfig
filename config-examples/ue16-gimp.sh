#!/bin/bash

# Copyright 2025 elluisian
#
# This file is subject to the BSD 3-Clause License.
# See the LICENSE file for details.



../ugeeconfig.sh from default-config.xml to gimp-config-ue16.xml set \
\
ue16.pen.button1.action_default 'mousek_sclick' \
ue16.pen.button2.action_default 'mousek_rclick' \
\
ue16.tablet.key1.action_custom.label 'Paintbrush' \
ue16.tablet.key1.action_custom.action 'keys(p)' \
ue16.tablet.key1.action_custom.enabled 'true' \
\
ue16.tablet.key2.action_custom.label 'Eraser' \
ue16.tablet.key2.action_custom.action 'keys(shift+e)' \
ue16.tablet.key2.action_custom.enabled 'true' \
\
ue16.tablet.key3.action_custom.label 'Toggle instruments' \
ue16.tablet.key3.action_custom.action 'keys(tab)' \
ue16.tablet.key3.action_custom.enabled 'true' \
\
ue16.tablet.key4.action_custom.label 'Toggle fullscreen' \
ue16.tablet.key4.action_custom.action 'keys(f11)' \
ue16.tablet.key4.action_custom.enabled 'true' \
\
ue16.tablet.key5.action_custom.label 'Rectangle selection' \
ue16.tablet.key5.action_custom.action 'keys(r)' \
ue16.tablet.key5.action_custom.enabled 'true' \
\
ue16.tablet.key6.action_custom.label 'Move objects' \
ue16.tablet.key6.action_custom.action 'keys(m)' \
ue16.tablet.key6.action_custom.enabled 'true' \
\
ue16.tablet.key7.action_custom.label 'Ctrl' \
ue16.tablet.key7.action_custom.action 'keys(ctrl)' \
ue16.tablet.key7.action_custom.enabled 'true' \
\
ue16.tablet.key8.action_custom.label 'Shift' \
ue16.tablet.key8.action_custom.action 'keys(shift)' \
ue16.tablet.key8.action_custom.enabled 'true' \
\
ue16.tablet.key9.action_default 'funct_swring1' \
\
ue16.tablet.r.selected_wheel 1 \
\
ue16.tablet.r.wheel_movement1.usage 'usg_custom' \
ue16.tablet.r.wheel_movement1.label 'Increase/decrease brush size' \
ue16.tablet.r.wheel_movement1.ccw_label 'Decrease' \
ue16.tablet.r.wheel_movement1.cw_label 'Increase' \
ue16.tablet.r.wheel_movement1.ccw_action 'keys(altgr+egrave)' \
ue16.tablet.r.wheel_movement1.cw_action 'keys(altgr+plus)' \
\
ue16.tablet.r.wheel_movement2.usage 'usg_custom' \
ue16.tablet.r.wheel_movement2.label 'Undo/Redo' \
ue16.tablet.r.wheel_movement2.ccw_label 'Undo last operation' \
ue16.tablet.r.wheel_movement2.cw_label 'Redo last operation' \
ue16.tablet.r.wheel_movement2.ccw_action 'keys(ctrl+z)' \
ue16.tablet.r.wheel_movement2.cw_action 'keys(ctrl+y)'