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
key_control = Keycode.CONTROL
key_command = Keycode.COMMAND
key_alt = Keycode.ALT

#xxxx = {"label": "xxx", "keys": [key_control, "c"]}

add = {"label": "add", "keys": ["git add .\n", key_enter]}
commit = {"label": "commit", "keys": ["git commit -m "]}
push = {"label": "push", "keys": ["git push origin "]}

pull = {"label": "pull", "keys": ["git pull origin "]}
main = {"label": "main", "keys": ["main\n"]}
dev = {"label": "dev", "keys": ["develop\n"]}

merge = {"label": "merge", "keys": ["git merge "]}
checkout = {"label": "checkout", "keys": ["git checkout"]}
b = {"label": "-b", "keys": ["-b"]}

status = {"label": "status", "keys": ["git status", key_enter]}
branch = {"label": "branch", "keys": ["git branch", key_enter]}
clone = {"label": "clone", "keys": ["git clone "]}

enc = {"label": "", "keys": [key_enter]}

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'git v2', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        #  (green, xxx["label"],xxx["keys"]),
        
        (green, add["label"],add["keys"]),
        (green, commit["label"],commit["keys"]),
        (green, push["label"],push["keys"]),

        # 2nd row ----------
        (green, pull["label"],pull["keys"]),
        (green, main["label"],main["keys"]),
        (green, dev["label"],dev["keys"]),
        
        # 3rd row ----------
        (green, merge["label"],merge["keys"]),
        (green, checkout["label"],checkout["keys"]),
        (green, b["label"],b["keys"]),
        
        # 4th row ----------
        (green, status["label"],status["keys"]),
        (green, branch["label"],branch["keys"]),
        (green, clone["label"],clone["keys"]),
        
        # Encoder button ---
        (green, enc["label"],enc["keys"]),
    ]
}
