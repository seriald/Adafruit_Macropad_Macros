# SPDX-FileCopyrightText: 2022 Robert Fleming
# Adapted from the VC Code Mac keypad by Jessica Calderon
# https://github.com/jessica-calderon/RP2040_Macros/blob/main/macros/mac-vscode.py
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
key_shift = Keycode.SHIFT

#xxxx = {"label": "xxx", "keys": [key_control, "c"]}


prefs = {"label": "prefs", "keys": [key_shift, key_command, "p"]}
open = {"label": "open", "keys": [key_command, "o"]}
settings = {"label": "sttings", "keys": [key_command, ","]}

all = {"label": "all", "keys": [key_control, "a"]}
cpy = {"label": "copy", "keys": [key_control, "c"]}
cut = {"label": "cut", "keys": [key_control, "x"]}
paste = {"label": "paste", "keys": [key_control, "v"]}

cmmt = {"label": "comment", "keys": [key_command, "/"]}
format = {"label": "format", "keys": [key_shift, key_alt, "f"]}

f_all = {"label": "f All", "keys": [key_shift, key_command, "f"]}
find = {"label": "find", "keys": [key_command, "f"]}
term = {"label": "term", "keys": [key_shift, key_control, "`"]}

enc = {"label": "", "keys": [key_control, key_shift, "A"]}

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Mac - VS Code', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (red, prefs["label"],prefs["keys"]),
        (red, open["label"],open["keys"]),
        (red, settings["label"],settings["keys"]),
        
        # 2nd row ----------
        (green, all["label"],all["keys"]),
        (green, cpy["label"],cpy["keys"]),
        (green, cut["label"],cut["keys"]),

        # 3rd row ----------
        (green, paste["label"],paste["keys"]),
        (teal, cmmt["label"],cmmt["keys"]),
        (teal, format["label"],format["keys"]),

        # 4th row ----------
        (teal, f_all["label"],f_all["keys"]),
        (teal, find["label"],find["keys"]),
        (blue, term["label"],term["keys"]),

        # Encoder ----------
        (black, enc["label"],enc["keys"]),
    ]
}