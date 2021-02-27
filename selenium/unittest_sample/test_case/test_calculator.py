import unittest

from calculator import Calculator


def setUpModule():
    print("test module start>>>")


def tearDownModule():
    print("test module end<<<")


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test class start>>>")

    @classmethod
    def tearDownClass(cls):
        print("test class end<<<")

    def setUp(self):
        print("\ntest start: ")

    def tearDown(self):
        print("test end!! ")

    def test_add(self):
        print("add")
        c = Calculator(5, 3)
        result = c.add()
        self.assertEqual(result, 8)

    def test_sub(self):
        print("sub")
        c = Calculator(5, 3)
        result = c.sub()
        self.assertEqual(result, 2)

    def test_mul(self):
        print("mul")
        c = Calculator(5, 3)
        result = c.mul()
        self.assertEqual(result, 15)

    def test_div(self):
        print("div")
        c = Calculator(10, 5)
        result = c.div()
        self.assertEqual(result, 2)


class TestCalculator1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test class start>>>")

    @classmethod
    def tearDownClass(cls):
        print("test class end<<<")

    def setUp(self):
        print("\ntest start: ")

    def tearDown(self):
        print("test end!! ")

    def test_add(self):
        print("add")
        c = Calculator(5, 3)
        result = c.add()
        self.assertEqual(result, 8)

    def test_sub(self):
        print("sub")
        c = Calculator(5, 3)
        result = c.sub()
        self.assertEqual(result, 2)

    def test_mul(self):
        print("mul")
        c = Calculator(5, 3)
        result = c.mul()
        self.assertEqual(result, 15)

    def test_div(self):
        print("div")
        c = Calculator(10, 5)
        result = c.div()
        self.assertEqual(result, 2)


unittest.main()

'''


if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator("test_add"))
    suit.addTest(TestCalculator("test_sub"))
    suit.addTest(TestCalculator("test_mul"))
    suit.addTest(TestCalculator("test_div"))

    runner = unittest.TextTestRunner()
    runner.run(suit)
'''
