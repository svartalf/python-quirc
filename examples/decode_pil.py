# -*- coding: utf-8 -*-

"""Decoding images using PIL for pre-processing"""

import sys

try:
    import Image
except ImportError:
    from PIL import Image

import quirc


if __name__ == '__main__':
    try:
        for code in quirc.decode(Image.open(sys.argv[1])):
            print code['text']
    except IndexError:
        print 'Usage: %s /path/to/qr/qr.image.jpg' % sys.argv[0]
