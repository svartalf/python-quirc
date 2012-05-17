# -*- coding: utf-8 -*_

import os.path
import unittest

def load_tests():
    return unittest.TestLoader().discover(os.path.dirname(__file__))