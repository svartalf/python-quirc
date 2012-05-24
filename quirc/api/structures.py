# -*- coding: utf-8 -*-

"""Mappings for the library structures"""

import ctypes

from quirc.api import constants


class Quirc(ctypes.Structure):
    """struct quirc;"""

    pass

QuircPointer = ctypes.POINTER(Quirc)


class Point(ctypes.Structure):
    """This structure describes a location in the input image buffer

    Map to `struct quirc_code`
    """

    _fields_ = (
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    )

PointPointer = ctypes.POINTER(Point)


class Code(ctypes.Structure):
    """This structure is used to return information about detected QR codes in the input image."""

    _fields_ = (
        ('corners', Point * 4),  # The four corners of the QR-code, from top left, clockwise
        ('size', ctypes.c_int),
        ('cell_bitmap', ctypes.c_uint8 * constants.MAX_BITMAP),
    )

CodePointer = ctypes.POINTER(Code)


class Data(ctypes.Structure):
    """This structure holds the decoded QR-code data"""

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
