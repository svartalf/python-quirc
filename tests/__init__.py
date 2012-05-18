# -*- coding: utf-8 -*_

import os.path

try:
    # For Python<2.7 use unitest2 for testing
    import unittest2 as unittest
except ImportError:
    import unittest

def load_tests():
    return unittest.TestLoader().discover(os.path.dirname(__file__))
