#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bindings to QR code decoding library `quirc`"""

__version__ = '0.1.0'
__all__ = ('version', 'new', 'destroy')

import ctypes
from ctypes.util import find_library

libquirc = ctypes.CDLL(find_library('quirc'), use_errno=True)

version = libquirc.quirc_version
version.restype = ctypes.c_char_p
version.__doc__ = '''Obtain the C library version string.'''


class Quirc(ctypes.Structure):
    """struct quirc;"""

    pass

QuircPointer = ctypes.POINTER(Quirc)

_new = libquirc.quirc_new
_new.argtypes = ()
_new.restype = QuircPointer

def new():
    """Construct a new QR-code recognizer.

    Instead of a C function, raises `MemoryError' if sufficient memory could not be allocated"""

    result = _new()
    if not result:
        raise MemoryError()

    return result

_destroy = libquirc.quirc_destroy
_destroy.argtypes = (QuircPointer,)
_destroy.restype = None

def destroy(structure):
    """Destroy a QR-code recognizer.

    TODO: attribute type check
    """

    _destroy(structure)