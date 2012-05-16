#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bindings to QR code decoding library `quirc`"""

__all__ = ('version',)

import ctypes
from ctypes.util import find_library

libquirc = ctypes.CDLL(find_library('quirc'), use_errno=True)

version = libquirc.quirc_version
version.restype = ctypes.c_char_p
version.__doc__ = '''Obtain the library version string.'''


class Quirc(ctypes.Structure):
    """struct quirc;"""

    pass

QuircPointer = ctypes.POINTER(Quirc)
