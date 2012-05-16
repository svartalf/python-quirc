# -*- coding: utf-8 -*-

import time
import unittest

import quirc


class TestQuirc(unittest.TestCase):

    def test_version(self):
        self.assertEqual(quirc.version(), '1.0')

    def test_creation(self):
        while True:
            try:
                obj = quirc.new()
                quirc.destroy(obj)
            except KeyboardInterrupt:
                return
            time.sleep(0.05)