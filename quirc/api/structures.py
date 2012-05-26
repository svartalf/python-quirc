# -*- coding: utf-8 -*-

"""Mappings for the library structures"""

import ctypes

from quirc.api import constants


class Quirc(ctypes.Structure):
    """QR code recognizer class

    Corresponds to `struct quirc <https://github.com/dlbeer/quirc/blob/master/lib/quirc.h#L22>`_.
    """

    pass

QuircPointer = ctypes.POINTER(Quirc)


class Point(ctypes.Structure):
    """This structure describes a location in the input image buffer

    Corresponds to `struct quirc_point <https://github.com/dlbeer/quirc/blob/master/lib/quirc.h#L56>`_.

    .. py:attribute:: x

    Value on the X axis

    .. py:attribute:: y

    Value on the Y axis
    """

    _fields_ = (
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    )

PointPointer = ctypes.POINTER(Point)


class Code(ctypes.Structure):
    """This structure is used to return information about detected QR codes in the input image.

    Corresponds to `struct quirc_code <https://github.com/dlbeer/quirc/blob/master/lib/quirc.h#L95>`_.

    .. py:attribute:: corners

    Array with the four corners of the QR code, from top left, clockwise.

    .. py:attribute:: size

    The number of cells across in the QR-code.

    .. py:attribute:: cell_bitmap

    The cell bitmap is a bitmask giving the actual values of cells.
    If the cell at ``(x, y)`` is black, then the following bit is set:
    ``cell_bitmap[i << 3] & (1 << (i & 7))`` where ``i = (y * size) + x``.
    """

    _fields_ = (
        ('corners', Point * 4),  # The four corners of the QR-code, from top left, clockwise
        ('size', ctypes.c_int),
        ('cell_bitmap', ctypes.c_uint8 * constants.MAX_BITMAP),
    )

CodePointer = ctypes.POINTER(Code)


class Data(ctypes.Structure):
    """This structure holds the decoded QR code data

    Corresponds to `struct quirc_data <https://github.com/dlbeer/quirc/blob/master/lib/quirc.h#L112>`_.

    .. py:attribute:: version

    QR code version

    .. py:attribute:: ecc_level

    Error correction code, which determines the degree of data redundancy.

    .. py:attribute:: mask

    .. py:attribute:: data_type

    .. py:attribute:: payload

     Data payload. For the Kanji datatype, payload is encoded as `Shift-JIS`. For all other datatypes, payload is `ASCII` text.

    .. py:attribute:: payload_len

    Length of the data payload.
    You can get a normal Python string from this binary data with a ``ctypes.string_at(data.payload, data.payload_len)``
    """

    _fields_ = (
        ('version', ctypes.c_int),
        ('ecc_level', ctypes.c_int),
        ('mask', ctypes.c_int),
        ('data_type', ctypes.c_int),

        # For the Kanji datatype, payload is encoded as Shift-JIS. For all other datatypes, payload is ASCII text.
        ('payload', ctypes.c_uint8*constants.MAX_PAYLOAD),
        ('payload_len', ctypes.c_int),
    )

DataPointer = ctypes.POINTER(Data)
