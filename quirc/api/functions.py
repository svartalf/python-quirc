#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ('version', 'new', 'destroy', 'resize', 'begin', 'end', 'count', 'extract', 'decode')

import ctypes
from ctypes.util import find_library

from quirc.api import constants
from quirc.api.exceptions import DecodeException
from quirc.api.structures import QuircPointer, CodePointer, DataPointer

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
    """Construct a new QR code recognizer.

    Do not forget to destroy in later with a `quirc.api.destroy`_ function.

    :raises: ``MemoryError`` if sufficient memory could not be allocated.
    :returns: ``quirc.api.structures.Quirc`` instance.
    """

    result = _new()
    if not result:
        raise MemoryError()

    return result

_destroy = libquirc.quirc_destroy
_destroy.argtypes = (QuircPointer,)
_destroy.restype = None


def destroy(recognizer):
    """Destroy a QR code recognizer.

    :param quirc.api.structures.Quirc recognizer: object, returned by `quirc.api.new`_ function.
    """

    if not isinstance(recognizer, QuircPointer):
        raise TypeError('Wrong type for recognizer parameter')

    _destroy(recognizer)

_resize = libquirc.quirc_resize
_resize.argtypes = (QuircPointer, ctypes.c_int, ctypes.c_int)
_resize.restype = ctypes.c_int


def resize(recognizer, width, height):
    """Resize the QR code recognizer.

    The size of an image must be specified before codes can be analyzed.

    :raises: ``MemoryError`` if sufficient memory could not be allocated.

    :param quirc.api.structures.Quirc recognizer: object, returned by `quirc.api.new`_ function.
    :param integer width: image width (in pixels)
    :param integer height: image height (in pixels)
    """

    if not isinstance(recognizer, QuircPointer):
        raise TypeError('Wrong type for recognizer parameter')

    # TODO: check parameters type for width and height

    result = _resize(recognizer, ctypes.c_int(width), ctypes.c_int(height))
    if result == -1:
        raise MemoryError()

_begin = libquirc.quirc_begin
_begin.argtypes = (QuircPointer, c_int_pointer, c_int_pointer)
_begin.restype = c_uint8_pointer


def begin(recognizer, width, height):
    """First part of the QR code recognition process.

    This function must be called firstly to obtain access to a buffer into which the input image should be placed.
    Returned buffer is a ctypes pointer to a allocated memory block. You need to format it with a image binary data.

    Width and height parameters must be equal to the parameters, applied to the function `quirc.api.begin`_.

    :param quirc.api.structures.Quirc recognizer: object, returned by `quirc.api.new`_ function.
    :param integer width: image width (in pixels)
    :param integer height: image height (in pixels)
    :returns: ctypes pointer to buffer
    """

    if not isinstance(recognizer, QuircPointer):
        raise TypeError('Wrong type for recognizer parameter')

    return _begin(recognizer, ctypes.byref(ctypes.c_int(width)), ctypes.byref(ctypes.c_int(height)))

_end = libquirc.quirc_end
_end.argtypes = (QuircPointer,)
_end.restype = None


def end(recognizer):
    """Must be called after filling the buffer to process the image for QR code recognition.

    :param quirc.api.structures.Quirc recognizer: object, returned by `quirc.api.new`_ function.
    """

    if not isinstance(recognizer, QuircPointer):
        raise TypeError('Wrong type for recognizer parameter')

    _end(recognizer)

_count = libquirc.quirc_count
_count.argtypes = (QuircPointer,)
_count.restype = ctypes.c_int


def count(recognizer):
    """Number of QR codes identified in the last processed image.

    :param quirc.api.structures.Quirc recognizer: object, returned by `quirc.api.new`_ function.
    :rtype: number of identified QR codes
    """

    if not isinstance(recognizer, QuircPointer):
        raise TypeError('Wrong type for recognizer parameter')

    return _count(recognizer)

_extract = libquirc.quirc_extract
_extract.argtypes = (QuircPointer, ctypes.c_int, CodePointer)
_extract.restype = ctypes.c_int


def extract(recognizer, idx, code):
    """Extract the QR code specified by the given index.

    Before calling this function, create object of a `Code` class, and it will be filled with a QR code information.

    :param quirc.api.structures.Quirc recognizer: object, returned by `quirc.api.new`_ function.
    :param integer idx: index of the recognized QR code.
    :param quirc.api.structures.Code code: instance of the ``Code`` class.
    """

    if not isinstance(recognizer, QuircPointer):
        raise TypeError('Wrong type for recognizer parameter')

    # TODO: parameter type check

    _extract(recognizer, idx, ctypes.byref(code))


def _decode_errcheck(result, func, arguments):
    if result:
        raise DecodeException(constants._DECODE_ERRORS[result])

_decode = libquirc.quirc_decode
_decode.argtypes = (CodePointer, DataPointer)
_decode.restype = ctypes.c_int  # TODO: return proper value
_decode.errcheck = _decode_errcheck


def decode(code, data):
    """Decode a QR code

    Fill instance of the ``quirc.api.structures.Data`` class with a QR code decoded data.

    :param quirc.api.structures.Code code: instance of the `Code` class.
    :param quirc.api.structures.Data data: instance of the `Data` class.
    """

    # TODO: parameter type check
    return _decode(ctypes.byref(code), ctypes.byref(data))
