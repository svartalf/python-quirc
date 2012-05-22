#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
from ctypes.util import find_library

from quirc.api.structures import QuircPointer, CodePointer

c_int_pointer = ctypes.POINTER(ctypes.c_int)
c_uint8_pointer = ctypes.POINTER(ctypes.c_uint8)

libquirc = ctypes.CDLL(find_library('quirc'))

version = libquirc.quirc_version
version.restype = ctypes.c_char_p
version.__doc__ = '''Obtain the C library version string.'''

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

    """

    # TODO: parameter type check

    _destroy(structure)

_resize = libquirc.quirc_resize
_resize.argtypes = (QuircPointer, ctypes.c_int, ctypes.c_int)
_resize.restype = ctypes.c_int

def resize(structure, width, height):
    """Resize the QR-code recognizer.

    The size of an image must be specified before codes can be analyzed."""

    # TODO: parameter type check

    result = _resize(structure, ctypes.c_int(width), ctypes.c_int(height))
    if result == -1:
        raise MemoryError()

_begin = libquirc.quirc_begin
_begin.argtypes = (QuircPointer, c_int_pointer, c_int_pointer)
_begin.restype = c_uint8_pointer

def begin(structure, width, height):
    # TODO: docstring
    # TODO: parameter type check

    return _begin(structure, ctypes.pointer(ctypes.c_int(width)), ctypes.pointer(ctypes.c_int(height)))

_end = libquirc.quirc_end
_end.argtypes = (QuircPointer,)
_end.restype = None

def end(structure):
    # TODO: docstring
    # TODO: parameter type check
    _end(structure)

_count = libquirc.quirc_count
_count.argtypes = (QuircPointer,)
_count.restype = ctypes.c_int

def count(structure):
    # TODO: docstring
    # TODO: parameter type check

    return _count(structure)

_extract = libquirc.quirc_extract
_extract.argtypes = (QuircPointer, ctypes.c_int, CodePointer)
_extract.restype = None

def extract(structure, idx, code):
    # TODO: doctring
    # TODO: parameter type check
    _extract(structure, idx, code)
