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
key_control = Keycode.CONTROL
key_command = Keycode.COMMAND
key_alt = Keycode.ALT
key_shift = Keycode.SHIFT
key_tab = Keycode.TAB

#xxxx = {"label": "xxx", "keys": [key_control, "c"]}

work = {"label": "work", "keys": ["", key_enter]}
w_user = {"label": "w user", "keys": [""]}
w_UPN = {"label": "w UPN", "keys": [""]}
wa = {"label": "admin", "keys": ["", key_enter]}
wa_UPN = {"label": "a UPN", "keys": [""]}
wa_user = {"label": "a user", "keys": [""]}
enter = {"label": "xxx", "keys": [key_enter]}
adm = {"label": "adm", "keys": ["", key_enter]}
home = {"label": "home", "keys": ["", key_enter]}

enc = {"label": "", "keys": [key_tab]}

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Auth', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (red, work["label"],work["keys"]),
        (black, enc["label"],enc["keys"]),
        (red, wa["label"],wa["keys"]),
        
        # 2nd row ----------
        (green, w_user["label"],w_user["keys"]),
        (black, enc["label"],enc["keys"]),
        (green, wa_user["label"],wa_user["keys"]),

        # 3rd row ----------
        (purple, w_UPN["label"],w_UPN["keys"]),
        (black, enc["label"],enc["keys"]),
        (purple, wa_UPN["label"],wa_UPN["keys"]),

        # 4th row ----------
        (teal, adm["label"],adm["keys"]),
         (black, enc["label"],enc["keys"]),
        (blue, home["label"],home["keys"]),

        # Encoder ----------
        (black, enc["label"],enc["keys"]),
    ]
}
