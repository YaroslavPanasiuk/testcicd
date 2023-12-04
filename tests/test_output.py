import unittest
from main import print_hi


# Test cases to test Calulator methods
# You always create  a child class derived from unittest.TestCase
class Test(unittest.TestCase):

    def test_output(self):
        self.assertEqual(print_hi("name"), "Hi, name")


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
