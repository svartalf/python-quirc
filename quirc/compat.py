# -*- coding: utf-8 -*-

"""Miscellaneous compatibility checks"""

# Image libraries
have_pil = True
try:
    from PIL import Image
except ImportError:
    try:
        import Image
    except ImportError:
        have_pil = False
