# SPDX-FileCopyrightText: 2022 Robert Fleming
#
# SPDX-License-Identifier: MIT

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

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

#xxxx = {"label": "xxx", "keys": [key_control, "c"]}

work = {"label": "work", "keys": ["xxxx", key_enter]}
w_user = {"label": "w user", "keys": ["xxxx"]}
w2 = {"label": "admin", "keys": ["xxxx", key_enter]}
w2_user = {"label": "admin u", "keys": ["xxxx"]}
enter = {"label": "xxx", "keys": [key_enter]}
xx = {"label": "xxx", "keys": ["xxxx", key_enter]}
home = {"label": "home", "keys": ["xxxx", key_enter]}

enc = {"label": "", "keys": [key_command, "w"]}

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Auth', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (red, work["label"],work["keys"]),
         (black, enc["label"],enc["keys"]),
        (red, w2["label"],w2["keys"]),
        
        # 2nd row ----------
        (green, w_user["label"],w_user["keys"]),
        (green, enc["label"],enc["keys"]),
        (green, w2_user["label"],w2_user["keys"]),

        # 3rd row ----------
         (black, enc["label"],enc["keys"]),
         (black, enc["label"],enc["keys"]),
         (black, enc["label"],enc["keys"]),

        # 4th row ----------
        (teal, xx["label"],xx["keys"]),
         (black, enc["label"],enc["keys"]),
        (blue, home["label"],home["keys"]),

        # Encoder ----------
        (black, enc["label"],enc["keys"]),
    ]
}