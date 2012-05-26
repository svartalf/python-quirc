#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bindings to QR code decoding library `quirc`"""

__version__ = '0.8.0'

import api
import converters
from base import decode, Decoder
from api.exceptions import DecodeException
