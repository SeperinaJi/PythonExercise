import unittest
from city_function import *

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        message = get_city_country('santiago', 'chile')
        self.assertEqual(message, 'Santiago Chile')

unittest.main()