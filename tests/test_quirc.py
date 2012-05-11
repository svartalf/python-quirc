# -*- coding: utf-8 -*-

import unittest

import quirc


class TestQuirc(unittest.TestCase):

    def test_version(self):
        self.assertEqual(quirc.version(), '1.0')
