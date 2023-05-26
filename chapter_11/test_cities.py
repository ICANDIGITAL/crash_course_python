import unittest
from city_functions import city_country


class CityFormatTester(unittest.TestCase):
    """Tests city_functions to find out if it outputs the correct string."""

    def test_city_country(self):
        """Tests city_functions to find out if it outputs the correct string."""
        formatted_city = city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_city_with_population = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_with_population, 'Santiago, Chile - 5000000')


