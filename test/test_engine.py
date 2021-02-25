import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from alphagrad.engine import Dual
class TestDualNumber(unittest.TestCase):
    def test_sin(self):
        self.assert_(Dual.sin(Dual(0,0)).r == 0)

    def test_cos(self):
        self.assert_(Dual.cos(Dual(0,0)).r == 1)

    def test_tan(self):
        self.assert_(Dual.tan(Dual(0,0)).r == 0)

    def test_exp(self):
        self.assert_(Dual.exp(Dual(0,0)).r == 1)

if __name__ == "__main__":
    unittest.main()
