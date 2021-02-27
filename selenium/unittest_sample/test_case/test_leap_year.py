import unittest
from leap_year import Leap_year

class TestLeapYear(unittest.TestCase):
    def setUp(self):
        print("\ntest start!!")
        
    def tearDown(self):
        print("test end!!")

    def test_loop_year_2000(self):
        result = Leap_year(2000).answer()
        self.assertEqual(result, "2000是闰年")

'''  
suit = unittest.TestSuite()
suit.addTest(TestLeapYear("test_loop_year_2000"))

runner = unittest.TextTestRunner()
runner.run(suit)
'''
