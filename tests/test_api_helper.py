# tests/test_api_helper.py

import unittest
from utils.api_helper import get_weather_data

class TestAPIHelper(unittest.TestCase):
    def test_get_weather_data(self):
        # You can mock API calls in a real test.
        result = get_weather_data("Delhi")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
