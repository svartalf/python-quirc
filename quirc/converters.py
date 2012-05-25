# -*- coding: utf-8 -*-

"""Converters from the external libraries image objects to the internal format

Handles convertion into a grayscale mode internally.
"""

import ctypes

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
