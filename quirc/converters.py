# -*- coding: utf-8 -*-

"""Converters from the external libraries image objects to the internal format

Handles convertion into a grayscale mode internally.
"""

import ctypes

def pil(image):
    """Convert the PIL.Image object to the pixels buffer

    Parameters::
        image : PIL.Image object
    """

    if image.mode not in ('1', 'L'):
        image = image.convert('L')
    width, height = image.size

    pixels = image.load()

    for i in range(width):
        for j in range(height):
            yield ctypes.c_uint8(pixels[j, i])
