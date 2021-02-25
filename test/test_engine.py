import unittest

import alphagrad

class TestDualNumber(unittest.TestCase):
    def test_cos():
        assert alphagrad.DualNumber.cos(alphagrad.DualNumber(0,0)).value == 1

if __name__ == "__main__":
    unittest.main()
