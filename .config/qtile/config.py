# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from typing import List  # noqa: F401

from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"

#==== Colors ====#

# Navy and Ivory - Snazzy based.
colors = [
    ["#021b21", "#021b21"],  # 0
    ["#032c36", "#065f73"],  # 1
    # ["#032c36", "#61778d"],# 1 this one is bit lighter, it is for inactive workspace icons.
    ["#e8dfd6", "#e8dfd6"],  # 2
    ["#c2454e", "#c2454e"],  # 3
    ["#44b5b1", "#44b5b1"],  # 4
    ["#9ed9d8", "#9ed9d8"],  # 5
    ["#f6f6c9", "#f6f6c9"],  # 6
    ["#61778d", "#61778d"],  # 7
    ["#e2c5dc", "#e2c5dc"],  # 8
    ["#5e8d87", "#5e8d87"],  # 9
    ["#032c36", "#032c36"],  # 10
    ["#2e3340", "#2e3340"],  # 11
    ["#065f73", "#065f73"],  # 12
    ["#8a7a63", "#8a7a63"],  # 13
    ["#A4947D", "#A4947D"],  # 14
    ["#BDAD96", "#BDAD96"],  # 15
    ["#a2d9b1", "#a2d9b1"],  # 16
]


powerline_symbol ="\u25e5"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Switch focus to specific monitor (out of three)
    Key([mod], "w", lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'),
    Key([mod], "e", lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Move the current column to the left or right
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating layout"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "Escape", lazy.spawn("slock"), desc="Lock the screen"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show run"),
        desc="Spawn a command using a prompt widget"),
]

groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label=""),
    Group("5", label=""),
    Group("6", label=""),
    Group("7", label=""),
    Group("8", label="﵂"),
    Group("9", label=""),
    Group("0", label=""),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
        #     desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus='#324c80', border_focus_stack='#92b19e', boder_normal='#191919', border_normal_stack='#191919', margin = 5, single_border_width = 0),
    layout.Max(),
    # Plasma(margin = 5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(margin = 5),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
#    font='monospace',
#    font='Ubuntu Mono',
    font='Iosevka Nerd Font',
#    foreground=colors["black"],
    fontsize=14,
    padding=0,
)
extension_defaults = widget_defaults.copy()

def top_bar():
    return [
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[6],
            foreground=colors[0],
        ),
        widget.GroupBox(
            font="Iosevka Nerd Font",
            fontsize=16,
            margin_y=3,
            margin_x=6,
            padding_y=7,
            padding_x=6,
            borderwidth=4,
            active=colors[8],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[3],
            highlight_method="block",
            this_current_screen_border=colors[6],
            block_highlight_text_color=colors[8],
            disable_drag=True,
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[0],
            foreground=colors[2],
        ),
        widget.WindowName(
            font="Iosevka Nerd Font",
            fontsize=15,
            background=colors[2],
            foreground=colors[0],
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[2],
            foreground=colors[0],
        ),
        widget.Spacer(length=200),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[0],
            foreground=colors[10],
        ),
        widget.Net(
            font="Iosevka Nerd Font",
            fontsize=15,
            format = '{down} ↓↑ {up}',
            background=colors[10],
            foreground=colors[2],
            padding=5,
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[10],
            foreground=colors[11],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize=18,
            padding=0,
            background=colors[11],
            foreground=colors[2],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("nautilus")},
        ),
        widget.DF(
            font="Iosevka Nerd Font",
            fontsize=15,
            partition="/home",
            format="{uf}{m} ({r:.0f}%)",
            visible_on_warn=False,
            background=colors[11],
            foreground=colors[2],
            padding=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("nautilus")},
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[11],
            foreground=colors[12],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize=16,
            foreground=colors[2],
            background=colors[12],
            padding=0,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e htop")},
        ),
        widget.Memory(
            background=colors[12],
            foreground=colors[2],
            font="Iosevka Nerd Font",
            fontsize=15,
            format="{MemUsed: .0f} MB",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e htop")},
        ),
        widget.Sep(
            padding=8,
            linewidth=0,
            background=colors[12],
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[12],
            foreground=colors[7],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[7],
        ),
        widget.KeyboardLayout(
            font="Iosevka Nerd Font",
            configured_keyboards=["us", "ch"],
            fontsize=15,
            padding=0,
            background=colors[7],
            foreground=colors[2],
        ),
        widget.Systray(
            background=colors[7],
            foreground=colors[2],
            icons_size=18,
            padding=4,
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[7],
            foreground=colors[13],
        ),
        widget.TextBox(
            text="墳 ",
            font="Iosevka Nerd Font",
            fontsize=18,
            background=colors[13],
            foreground=colors[0],
        ),
        widget.Volume(
            background=colors[13],
            foreground=colors[0],
            font="Iosevka Nerd Font",
            fontsize=15,
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
        ),
        # Doesn't work with Spotify so its disabled!
        # widget.TextBox(
        #    text="\u2572",
        #    font="Inconsolata for powerline",
        #    fontsize="33",
        #    padding=0,
        #    background=colors[13],
        #    foreground=colors[0],
        # ),
        # widget.Mpd2(
        #   background=colors[13],
        #   foreground=colors[0],
        #   idle_message=" ",
        #   idle_format="{idle_message} Not Playing",
        #   status_format="  {artist}/{title} [{updating_db}]",
        #   font="Iosevka Nerd Font",
        #   fontsize=15,
        # ),
        # This one works with Spotify, enable if you want!
        # widget.Mpris2(
        #    background=colors[13],
        #    foreground=colors[0],
        #    name="spotify",
        #    objname="org.mpris.MediaPlayer2.spotify",
        #    fmt="\u2572   {}",
        #    display_metadata=["xesam:title", "xesam:artist"],
        #    scroll_chars=20,
        #    font="Iosevka Nerd Font",
        #    fontsize=15,
        # ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[13],
            foreground=colors[14],
        ),
        widget.Battery(
            font="Iosevka Nerd Font",
            charge_char="",
            discharge_char="",
            empty_char="",
            format="{char} {percent:2.0%}",
            background=colors[14],
            foreground=colors[0],
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[14],
            foreground=colors[15],
        ),
        widget.TextBox(
            text="   ",
            font="Iosevka Nerd Font",
            fontsize="14",
            padding=0,
            background=colors[15],
            foreground=colors[0],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            foreground=colors[0],
            background=colors[15],
            fontsize=15,
            format="%d %b, %A",
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[15],
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[15],
            foreground=colors[16],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize="18",
            padding=0,
            background=colors[16],
            foreground=colors[0],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            foreground=colors[0],
            background=colors[16],
            fontsize=15,
            format="%H:%M",
        ),
        widget.TextBox(
            text=powerline_symbol,
            font="Inconsolata for powerline",
            fontsize=42,
            padding=0,
            background=colors[16],
            foreground=colors[6],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
    ]

screens = [
    Screen(
        top=bar.Bar(
            top_bar(),
            size=22,
            background=colors[0],
            margin=[0, 0, 0, 0],
            opacity=0.95
        ),
        wallpaper="~/Pictures/wallpaper.jpg",
        wallpaper_mode="fill",
    ),
    Screen(
        wallpaper="~/Pictures/wallpaper.jpg",
        wallpaper_mode="fill",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='Qalculate!'),  # qalculate-gtk
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    subprocess.call(os.path.expanduser('~/.config/qtile/autostart.sh'))

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
