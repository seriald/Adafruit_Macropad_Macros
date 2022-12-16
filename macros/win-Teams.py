# SPDX-FileCopyrightText: 2022 Jessica Calderon
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: git terminal commands

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
key_return = Keycode.RETURN
key_control = Keycode.CONTROL
key_command = Keycode.COMMAND
key_tab = Keycode.TAB
key_alt = Keycode.ALT
key_slash = Keycode.FORWARD_SLASH
key_space = Keycode.SPACE

#xxxx = {"label": "xxx", "keys": [key_control, "c"]}
search = {"label": "???", "keys": [key_control, "e", key_enter]}
mentions = {"label": "Mentions", "keys": [key_control, "e", key_slash, "mentions", 0.25, key_enter]}
files = {"label": "Files", "keys": [key_control, "e", key_slash, "files", 0.25, key_enter]}
enc = {"label": "", "keys": [key_enter]}

# status
dnd = {"label": "DND", "keys": [key_control, "e/dnd", 0.25, key_enter]}
avail = {"label": "avail", "keys": [key_control, "e", key_slash, "available", 0.25, key_enter]}
brb = {"label": "BRB", "keys": [key_control, "e", key_slash, "brb", 0.25, key_enter]}

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'teams', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        #  (green, xxx["label"],xxx["keys"]),
        (green, dnd["label"],dnd["keys"]),
        (black, enc["label"],enc["keys"]),
        (blue, search["label"],search["keys"]),

        # 2nd row ----------
        (green, avail["label"],avail["keys"]),
        (teal, mentions["label"],mentions["keys"]),
        (black, enc["label"],enc["keys"]),
        
        # 3rd row ----------
        (green, brb["label"],brb["keys"]),
        (teal, files["label"],files["keys"]),
        (black, enc["label"],enc["keys"]),
        
        # 4th row ----------
        (black, enc["label"],enc["keys"]),
        (black, enc["label"],enc["keys"]),
        (black, enc["label"],enc["keys"]),
        
        # Encoder button ---
        (black, enc["label"],enc["keys"]),
    ]
}
