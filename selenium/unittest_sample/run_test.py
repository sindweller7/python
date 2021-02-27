import unittest

test_dir = "./test_case"
suits = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__  == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suits)
