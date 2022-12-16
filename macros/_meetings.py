# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Adobe Photoshop for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Meetings', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x83232, 'Mic+-', [Keycode.CONTROL, Keycode.SHIFT, 'M']),
        (0x303030, 'Hand', [Keycode.CONTROL, Keycode.SHIFT, 'K']),
        (0x811dbf, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0x83232, 'Vid+-', [Keycode.CONTROL, Keycode.SHIFT, 'O']),     # Default colors
        (0x303030, 'Share', [Keycode.CONTROL, Keycode.SHIFT, 'E']),
        (0x811dbf, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        # 3rd row ----------
        (0x004000, 'Accept', [Keycode.CONTROL, Keycode.SHIFT, 'A']),
        (0x900000, 'End', [Keycode.CONTROL, Keycode.SHIFT, 'H']),
		(0x000000, ' ', 'W'),
        # 4th row ----------
        (0x004000, 'Join ', [Keycode.CONTROL, Keycode.SHIFT, 'J']),
        (0x000000, ' ', 'x'),
		(0x811dbf, 'Mute', [[ConsumerControlCode.MUTE]]),		
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.SHIFT, 'A']),
    ]
}
