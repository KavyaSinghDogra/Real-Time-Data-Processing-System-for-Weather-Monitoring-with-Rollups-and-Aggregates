# tests/test_database_helper.py

import unittest
from utils.database_helper import store_daily_summary

class TestDatabaseHelper(unittest.TestCase):
    def test_store_daily_summary(self):
        summary = {
            'date': '2024-10-20',
            'avg_temp': 30.0,
            'max_temp': 35.0,
            'min_temp': 25.0,
            'dominant_condition': 'Clear'
        }
        store_daily_summary(summary)
        # Additional checks can be added here.

if __name__ == '__main__':
    unittest.main()
