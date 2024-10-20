# tests/test_alerts.py

import unittest
from utils.alerts import check_alerts

class TestAlerts(unittest.TestCase):
    def test_check_alerts(self):
        weather_data = {'main': {'temp': 36}, 'name': 'Delhi'}
        # You can redirect output to test alerts.
        check_alerts(weather_data)

if __name__ == '__main__':
    unittest.main()
