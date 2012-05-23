# -*- coding: utf-8 -*-

import os.path
import unittest

import quirc

USING_PIL = True
try:
    import Image
except ImportError:
    try:
        from PIL import Image
    except ImportError:
        USING_PIL = False


class TestQuircCase(unittest.TestCase):

    def setUp(self):
        self._folder = os.path.abspath(os.path.dirname(__file__))

    @unittest.skipIf(not USING_PIL, 'PIL is unaccessible')
    def test_pil(self):
        image = Image.open(os.path.join(self._folder, 'images', 'link.gif'))

        result = list(quirc.decode(image))

        self.assertEqual(len(result), 1)

        code = result[0]

        self.assertEqual(code['data_type'], 4)
        self.assertEqual(code['mask'], 6)
        self.assertEqual(code['ecc_level'], 0)
        self.assertEqual(code['size'], 29)

        self.assertTupleEqual(code['corners'], ((16, 16), (132, 16), (132, 132), (16, 132)))
        self.assertEqual(code['text'], 'https://github.com/svartalf/python-quirc')
