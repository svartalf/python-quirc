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
        # We need a black/white image
        if image.mode != '1':
            image = image.convert('1')
        # Make a pixel access object (http://effbot.org/zone/pil-pixel-access.htm)
        pixels = image.load()
        width, height = image.size

        # Unwrap an 2d array into a flat bytes array
        flat = (ctypes.c_int*(width*height))()
        idx = 0
        for i in xrange(height):
            for j in xrange(width):
                flat[idx] = pixels[i, j]
                idx += 1

        obj = quirc.new()
        quirc.resize(obj, 115, 115)
        buffer = quirc.begin(obj, 115, 115)
        buffer.contents = flat
        quirc.end(obj)
        quirc.destroy(obj)
