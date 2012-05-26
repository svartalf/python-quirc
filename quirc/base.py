# -*- coding: utf-8 -*-

import ctypes

import api
import compat
import converters

if compat.have_pil:
    try:
        import Image
    except ImportError:
        from PIL import Image


class Code(object):
    """Structure for storing extracted QR code data"""

    __slots__ = ('corners', 'size', 'version', 'ecc_level', 'data_type', 'text')

    def __init__(self, corners, size, version, ecc_level, data_type, text):
        self.corners = corners
        self.size = size
        self.version = version
        self.ecc_level = ecc_level
        self.data_type = data_type
        self.text = text

    def __repr__(self):
        return self.text


def decode(image):
    """Recognize image and return generator with all the available QR codes

    Currently supports only PIL Image object as an parameter
    """

    # TODO: `image` type check

    # Convert to grayscale mode
    if image.mode not in ('1', 'L'):
        image = image.convert('L')

    width, height = image.size
    pixels = image.load()

    obj = api.new()
    api.resize(obj, width, height)
    buffer = api.begin(obj, width, height)

    # Fill buffer with a image pixels. One cell, one pixel.
    for idx, pixel in enumerate(converters.pil(image)):
        buffer[idx] = pixel

    # Finish codes identification
    api.end(obj)

    code = api.structures.Code()
    data = api.structures.Data()

    for i in range(api.count(obj)):

        # Extract first code
        api.extract(obj, i, code)
        api.decode(code, data)

        yield Code(
            tuple([(corner.x, corner.y) for corner in code.corners]),
            code.size,
            data.version,
            data.ecc_level,
            data.data_type,
            ctypes.string_at(data.payload, data.payload_len),
        )

    api.destroy(obj)


class Decoder(object):

    def __init__(self, width, height):
        self._width = width
        self._height = height

        self._obj = api.new()
        api.resize(self._obj, self._width, self._height)

        self._code = api.structures.Code()
        self._data = api.structures.Data()

    def decode(self, data):
        """Fill buffer with a raw binary data

        Each byte already must represent one pixel

        Parameters::

            data : image binary data
        """

        buffer = api.begin(self._obj, self._width, self._height)

        converters.raw(buffer, data)

        api.end(self._obj)

        for i in range(api.count(self._obj)):

            # Extract first code
            api.extract(self._obj, i, self._code)
            try:
                api.decode(self._code, self._data)
            except api.exceptions.DecodeException:
                continue

            yield Code(
                tuple([(corner.x, corner.y) for corner in self._code.corners]),
                self._code.size,
                self._data.version,
                self._data.ecc_level,
                self._data.data_type,
                ctypes.string_at(self._data.payload, self._data.payload_len),
            )

    def __del__(self):
        api.destroy(self._obj)
