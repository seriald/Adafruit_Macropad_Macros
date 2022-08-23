# SPDX-FileCopyrightText: 2022 Robert Fleming
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
key_up = Keycode.UP_ARROW
key_down = Keycode.DOWN_ARROW
key_Right = Keycode.RIGHT_ARROW
key_Left = Keycode.LEFT_ARROW

#xxxx = {"label": "xxx", "keys": [key_control, "c"]}

AI_on = {"label": "AI ", "keys": [key_alt, "l"]}
ZoomOut = {"label": "+", "keys": [key_alt, "i"]}
ZoomIn = {"label": "-", "keys": [key_alt, "o"]}
ZoomMax = {"label": "Max", "keys": [key_alt, "j"]}
ZoomMin = {"label": "Min", "keys": [key_alt, "k"]}
TiltUp = {"label": "Up", "keys": [key_alt, key_up]}
TiltDown = {"label": "Down", "keys": [key_alt, key_down]}
TiltRght = {"label": "Right", "keys": [key_alt, key_Right]}
TiltLeft = {"label": "Left", "keys": [key_alt, key_Left]}
GimbalReset = {"label": "", "keys": [key_alt, "r"]}
Sleep = {"label": "Sleep", "keys": [key_alt, "t"]}
PSN1 = {"label": "", "keys": [key_alt, "q"]}


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

enc = {"label": "", "keys": [key_control, "l"]}

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'OBSbot', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (red, AI_on["label"],AI_on["keys"]),
        (purple, ZoomMin["label"],ZoomMin["keys"]),
        (purple, ZoomMax["label"],ZoomMax["keys"]),
        
        # 2nd row ----------
        (green, ZoomIn["label"],ZoomIn["keys"]),
        (teal, TiltUp["label"],TiltUp["keys"]),
        (black, PSN1["label"],PSN1["keys"]),

        # 3rd row ----------
        (teal, TiltLeft["label"],TiltLeft["keys"]),
        (black, GimbalReset["label"],GimbalReset["keys"]),
        (teal, TiltRght["label"],TiltRght["keys"]),

        # 4th row ----------
        (green, ZoomOut["label"],ZoomOut["keys"]),
        (teal, TiltDown["label"],TiltDown["keys"]),
        (red, Sleep["label"],Sleep["keys"]),

        # Encoder ----------
        (black, enc["label"],enc["keys"]),
    ]
}
