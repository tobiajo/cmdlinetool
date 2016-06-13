import unittest
from cmdlinetool import util


class TestUtil(unittest.TestCase):
    def test_adder(self):
        self.assertEqual(util.adder(3, 5), 8)

    def test_adder2(self):
        self.assertEqual(util.adder(-3, -5), -8)
