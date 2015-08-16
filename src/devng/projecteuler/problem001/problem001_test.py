from problem001 import *
import unittest

class Problem001Test(unittest.TestCase):
    def test_sum_n(self):
        sum10 = sum_n(10)
        self.assertEqual(sum10, 55)

    	sum1000 = sum_n(1000)
        self.assertEqual(sum1000, 500500)

    def test_sum35(self):
        sum10 = sum_3_5(10)
        self.assertEqual(sum10, 23)

    	sum1000 = sum_3_5(1000)
        self.assertEqual(sum1000, 233168)

if __name__ == '__main__':
    unittest.main()
