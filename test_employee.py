import unittest
from employee import *

class TestEmployeeCase(unittest.TestCase):
    def setUp(self):
        self.emoplyee = Employee('jony', 'ma', 5000)

    def test_give_default_raise(self):
        self.emoplyee.give_raise()
        self.assertEqual(5500, self.emoplyee.salary)

    def test_give_custom_raise(self):
        self.emoplyee.give_raise(1000)
        self.assertEqual(6000, self.emoplyee.salary)

unittest.main()