# -*- coding: utf-8 -*-

import os.path
import ctypes
import unittest

import quirc


class TestQuirc(unittest.TestCase):

    def setUp(self):
        self._folder = os.path.abspath(os.path.dirname(__file__))

    def test_version(self):
        self.assertEqual(quirc.api.version(), '1.0')

    def test_creation(self):
        obj = quirc.api.new()
        quirc.api.resize(obj, 640, 480)
        quirc.api.destroy(obj)

    def test_fill(self):
        """Test filling image buffer

        Example file `tests/images/test1.bin' contains already prepared data, where each symbol represents one pixel.
        This a copy of the `tests/images/test1.png' file data. Width and height size are equal to 115px.
        """

        pixels = open(os.path.join(self._folder, 'images', 'test1.bin')).read()
        width = height = 115

        obj = quirc.api.new()
        quirc.api.resize(obj, width, height)
        buffer = quirc.api.begin(obj, width, height)

        # Fill buffer with a image pixels. One cell, one pixel.
        for idx, pixel in enumerate(pixels):
            buffer[idx] = ctypes.c_uint8(ord(pixel))

        quirc.api.end(obj)

        amount = quirc.api.count(obj)
        self.assertEqual(amount, 1)

        quirc.api.destroy(obj)
