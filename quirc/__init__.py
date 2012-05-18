#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bindings to QR code decoding library `quirc`"""

__version__ = '0.2.0'
__all__ = ('version', 'new', 'destroy')

import ctypes
from ctypes.util import find_library

libquirc = ctypes.CDLL(find_library('quirc'))

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

_resize = libquirc.quirc_resize
_resize.argtypes = (QuircPointer, ctypes.c_int, ctypes.c_int)
_resize.restype = ctypes.c_int

def resize(structure, width, height):
    """Resize the QR-code recognizer.

    The size of an image must be specified before codes can be analyzed."""

    result = _resize(structure, width, height)
    if result == -1:
        raise MemoryError()

