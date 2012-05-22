# -*- coding: utf-8 -*-

import os.path
import ctypes
import unittest

import quirc


class TestQuirc(unittest.TestCase):

    def setUp(self):
        self._folder = os.path.abspath(os.path.dirname(__file__))

    def test_version(self):
        self.assertEqual(quirc.version(), '1.0')

    def test_creation(self):
        obj = quirc.new()
        quirc.resize(obj, 640, 480)
        quirc.destroy(obj)

    def test_pil_fill(self):
        """Test filling image buffer with a PIL

        Example file `tests/images/test1.png'
        """

        try:
            import Image
        except ImportError:
            from PIL import Image

        image = Image.open(os.path.join(self._folder, 'images', 'test1.png'))
        # We need a grayscale image
        if image.mode not in ('1', 'L'):
            image = image.convert('L')

        # Make a pixel access object (http://effbot.org/zone/pil-pixel-access.htm)
        pixels = image.load()
        width, height = image.size

        obj = quirc.new()
        quirc.resize(obj, width, height)
        buffer = quirc.begin(obj, width, height)

        # Fill buffer with a image pixels. One cell, one pixel.
        idx = 0
        for i in xrange(height):
            for j in xrange(width):
                buffer[idx] = ctypes.c_uint8(pixels[i, j])
                idx += 1

        quirc.end(obj)

        amount = quirc.count(obj)
        self.assertEqual(amount, 1)

        quirc.destroy(obj)
