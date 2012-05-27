# -*- coding: utf-8 -*-

"""Miscellaneous compatibility checks"""

import sys


range = range if sys.version_info[0] == 3 else xrange

# Image libraries
have_pil = True
try:
    from PIL import Image
except ImportError:
    try:
        import Image
    except ImportError:
        have_pil = False


class Mock(object):
    """Simple mock object for replacing `libquirc` library while building a docs on the readthedocs.org"""

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            return type(name, (), {})
        else:
            return Mock()
