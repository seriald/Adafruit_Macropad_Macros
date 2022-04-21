# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Adobe Photoshop for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Auth', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Work', ['xxxx', Keycode.ENTER]),
        (0x000000, '', ''),
        (0x000040, 'Admin', ['xxxx', Keycode.ENTER]),
        # 2nd row ----------
        (0x000000, '', ''),
        (0x2d53b3, 'Enter', [Keycode.ENTER]),
        (0x000000, '', ''),
        # 3rd row ----------
        (0x000000, '', ''),
        (0x000000, '', ''),
        (0x000000, '', ''),
        # 4th row ----------
        (0x000000, '', ''),
        (0x000000, '', ''),
        (0x83232, 'Home ', ['xxxx', Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.ALT, 'S']) # Save for web
    ]
}
