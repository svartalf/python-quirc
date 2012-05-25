# -*- coding: utf-8 -*-

import os.path
try:
    import unittest2 as unittest # For Python<=2.6
except ImportError:
    import unittest

import quirc
from quirc import compat

if compat.have_pil:
    try:
        import Image
    except ImportError:
        from PIL import Image


class TestQuircCase(unittest.TestCase):

    def setUp(self):
        self._folder = os.path.abspath(os.path.dirname(__file__))

    def test_decoder(self):
        decoder = quirc.Decoder(148, 148)
        decoder.decode(Image.open(os.path.join(self._folder, 'images', 'link.gif')))

    @unittest.skipIf(not compat.have_pil, 'PIL is unaccessible')
    def test_pil(self):
        try:
            import Image
        except ImportError:
            from PIL import Image

        image = Image.open(os.path.join(self._folder, 'images', 'link.gif'))

        result = list(quirc.decode(image))

        self.assertEqual(len(result), 1)

        code = result[0]

        self.assertEqual(code.data_type, 4)
        self.assertEqual(code.ecc_level, 0)
        self.assertEqual(code.size, 29)

        self.assertTupleEqual(code.corners, ((16, 16), (132, 16), (132, 132), (16, 132)))
        self.assertEqual(code.text, str(code), 'https://github.com/svartalf/python-quirc')
