# -*- coding: utf-8 -*-

import time
import unittest

import quirc


class TestQuirc(unittest.TestCase):

    def test_version(self):
        self.assertEqual(quirc.version(), '1.0')

    def test_creation(self):
        obj = quirc.new()
        quirc.resize(obj, 640, 480)
        quirc.destroy(obj)
