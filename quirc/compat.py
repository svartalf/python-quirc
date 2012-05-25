# -*- coding: utf-8 -*-

"""Miscellaneous compatibility checks"""

import sys


range = range if sys.version_info[0] == 3 else xrange

# Image libraries
have_pil = True
try:
    from PIL import Image
except ImportError:
    try:
        import Image
    except ImportError:
        have_pil = False
