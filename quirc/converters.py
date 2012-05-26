# -*- coding: utf-8 -*-

"""Converters from the external libraries image objects to the internal format

Handles convertion into a grayscale mode internally.
"""

import ctypes
import array

from compat import range


def pil(image):
    """Convert the PIL.Image object to the pixels buffer

    Parameters::
        image : PIL.Image object
    """

    if image.mode not in ('1', 'L'):
        image = image.convert('L')
    width, height = image.size

    pixels = image.load()

    width_iter = range(width)
    height_iter = range(height)

    for i in width_iter:
        for j in height_iter:
            yield ctypes.c_uint8(pixels[j, i])


def raw(buffer, data):
    """Fill the buffer with a raw binary data

    Parameters::
        buffer : returned by the `quirc.api.begin` function object
        data : binary data
    """

    buf = array.array('B', data)
    ctypes.memmove(buffer, buf.buffer_info()[0], len(data))
