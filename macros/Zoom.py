# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Adobe Photoshop for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Zoom', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Mic+-', [Keycode.ALT, Keycode.A]),
        (0x101010, 'Hand', [Keycode.ALT, Keycode.Y]),
        (0x000040, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0x004000, 'Vid+-', [Keycode.ALT, Keycode.V]),     # Default colors
        (0x000000, 'Thumbs Up ', 'M'), # Cycle rect/ellipse marquee (select)
        (0x000040, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        # 3rd row ----------
        (0x000000, ' ', 'x'),    # Swap foreground/background colors
        (0x000000, ' ', 'v'),    # Move layer
        (0x000040, 'Mute', [[ConsumerControlCode.MUTE]]),
        # 4th row ----------
        (0x004000, 'Share', [Keycode.CONTROL, Keycode.SHIFT, 'E']), # Cycle eyedropper/measure modes
        (0x000000, ' ', 'W'),    # Cycle "magic wand" (selection) modes
        (0x000000, 'End', [Keycode.ALT, Keycode.Q,Keycode.ENTER]),    # Cycle "healing" modes
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.ALT, 'S']) # Save for web
    ]
}
