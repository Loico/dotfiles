#!/usr/bin/env bash

# Network Manager applet
nm-applet &

# Redshift applet
redshift-gtk &

# Compositor
picom -b --experimental-backends

# Swap caps lock and escape keys
xmodmap ~/.config/qtile/.speedswapper
