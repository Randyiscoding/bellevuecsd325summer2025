# --------------------------------------------------------
# Name: Randy Easton
# Date: 6/28/2025
# Assignment: Module 7.2 Assignment: Test Cases
# --------------------------------------------------------
# Purpose:
# [Brief one-sentence description of what the program does]
# --------------------------------------------------------

import unittest
from city_functions import  citycountry
class testing(unittest.TestCase):
    def test_city_country(self):
        """
        Test citycountry() with basic city and country input
        """
        formatted_location = citycountry('santiago', 'chile')
        self.assertEqual(formatted_location, 'santiago, chile')
        pass


# Program starts here
if __name__ == "__main__":
    main()
