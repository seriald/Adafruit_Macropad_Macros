# SPDX-FileCopyrightText: 2022 Robert Fleming
# Adapted from the vim keypad by Cristina Solana
# https://github.com/CristinaSolana/adafruit-macropad-vim-macros/blob/main/vim.py
#
# SPDX-License-Identifier: MIT

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

#Opening / Closing
open_nano = {"label": "open", "keys": ["nano", key_enter]}
close = {"label": "close", "keys": [key_control, "x"]}

#Misc
cancel = {"label": "cancel", "keys": [key_control, "c"]}
pgup = {"label": "pg up", "keys": [key_control, "y"]}
pgdn = {"label": "pg dwn", "keys": [key_control, "v"]}

# Files
find = {"label": "find", "keys": [key_control, "w"]}

# Writing Changes. It's easy!
write = {"label": "write", "keys": [key_control, "o", key_enter]}
write_close = {"label": "wclose", "keys": [key_control, "o", key_enter, key_control, "x"]}


app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'nano', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (green, open_nano["label"], open_nano["keys"]),
        (teal, find["label"], find["keys"]),
        (red,pgup["label"], pgup["keys"]),
        # 2nd row ----------
        (white, close["label"], close["keys"]),
        (black, "", [key_command, "w"]),  # Close window/tab
        (red,pgdn["label"], pgdn["keys"]),

        # 3rd row ----------
        (black, cancel["label"],cancel["keys"]),
        (black, "", [key_command, "w"]),  # Close window/tab
        (black, "", [key_command, "w"]),  # Close window/tab
        # 4th row ----------
        (black, "", [key_command, "w"]),  # Close window/tab
        (green, write["label"], write["keys"]),
        (hot_pink, write_close["label"], write_close["keys"]),
        # Encoder ----------
        (black, "", [key_command, "w"]),  # Close window/tab
    ]
}