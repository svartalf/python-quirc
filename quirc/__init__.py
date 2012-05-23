#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bindings to QR code decoding library `quirc`"""

import ctypes

from quirc import api

USING_PIL = True
try:
    from PIL import Image
except ImportError:
    try:
        import Image
    except ImportError:
        USING_PIL = False

__version__ = '0.6.1'
__all__ = ('api', 'decode')


def decode(image):
    """Recognize image and return generator with all the available QR codes

    Currently supports only PIL Image object as an parameter
    """

    if not (USING_PIL and isinstance(image, Image.Image)):
        raise TypeError('Unknown image object type: %s' % type(image))

    # Convert to grayscale mode
    if image.mode not in ('1', 'L'):
        image = image.convert('L')

    width, height = image.size
    pixels = image.load()

    obj = api.new()
    api.resize(obj, width, height)
    buffer = api.begin(obj, width, height)

    # Fill buffer with a image pixels. One cell, one pixel.
    # TODO: looks like a very slow operation
    idx = 0
    for i in range(width):
        for j in range(height):
            buffer[idx] = ctypes.c_uint8(pixels[j, i])
            idx += 1

    del idx

    # Finish codes identification
    api.end(obj)

    num_codes = api.count(obj)

    code = api.structures.Code()
    data = api.structures.Data()

    for i in range(num_codes):

        # Extract first code
        api.extract(obj, i, code)
        api.decode(code, data)

        yield {
            'corners': tuple([(corner.x, corner.y) for corner in code.corners]),
            'size': code.size,
            'version': data.version,
            'ecc_level': data.ecc_level,
            'mask': data.mask,
            'data_type': data.data_type,
            'text': ctypes.string_at(data.payload, data.payload_len),
        }

    api.destroy(obj)
