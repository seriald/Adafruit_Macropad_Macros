# SPDX-FileCopyrightText:
#
# SPDX-License-Identifier: MIT

# MS Teams Hotkeys (MacOS)

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Colors | Find more at: https://www.color-hex.com/
black = 0x000000
white = 0x101010
red = 0xFF0000
green = 0x8CFF00
blue = 0x000040
yellow = 0xFFC100
purple = 0xBE29EC
hot_pink = 0xff1177
teal = 0x07EAA1

# Keys | API docs: 
# https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html

key_enter = Keycode.ENTER
key_control = Keycode.CONTROL
key_command = Keycode.COMMAND
key_alt = Keycode.ALT
key_shift = Keycode.SHIFT
Cons_mute = ConsumerControlCode.MUTE
Cons_vdown = ConsumerControlCode.VOLUME_DECREMENT
Cons_vup = ConsumerControlCode.VOLUME_INCREMENT

#xxxx = {"label": "xxx", "keys": [key_control, "c"]}

audio = {"label": "audio", "keys": [key_command, key_shift, "M"]}
chat = {"label": "chat", "keys": [key_command, "2"]}
video = {"label": "video", "keys": [key_command, key_shift, "0"]}
share = {"label": "share", "keys": [key_command, key_shift, "E"]}
leave = {"label": "leave", "keys": [key_command, key_shift, "H"]}

mute = {"label": "mute", "keys": [Cons_mute]}
vup = {"label": "vol +", "keys": [Cons_vup]}
vdown = {"label": "vol -", "keys": [Cons_vdown]}

enc = {"label": "", "keys": [key_control, key_shift, "A"]}

app = {
    'name' : 'Mac - Teams', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (green, audio["label"], audio["keys"]),
        (teal, chat["label"], chat["keys"]),
        (red,video["label"], video["keys"]),
        # 2nd row ----------
        (white, share["label"], share["keys"]),
        (black,enc["label"], enc["keys"]),
        (red,leave["label"], leave["keys"]),

        # 3rd row ----------
        (black,enc["label"], enc["keys"]),
        (black,enc["label"], enc["keys"]),
        (green,vup["label"], vup["keys"]),
        # 4th row ----------
        (black, "", [key_command, "w"]),  # Close window/tab
        (red, mute["label"], mute["keys"]),
        (green, vdown["label"], vdown["keys"]),
        # Encoder ----------
        (black,enc["label"], enc["keys"]),
    ]
}
