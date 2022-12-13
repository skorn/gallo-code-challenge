from app import setup_db, regions, region, locations, location, weather
import unittest

from urllib import request

class TestRegions(unittest.TestCase):
    def setUp(self):
        setup_db()
        self.expected_regions = [('Coastal',), ('Valley',), ('Southern',)]
        self.expected_region = [('BORDEN HILLS',),
            ('COWELL RANCH',),
            ('LIBERTY LODI',),
            ('LIVINGSTON RANCHES',),
            ('VALLEY OAK',)]
        self.expected_locations = [('Coastal', 'BARRELLI CREEK'),
            ('Coastal', 'FREI RANCH'),
            ('Coastal', 'MONTE ROSSO'),
            ('Coastal', 'WILLIAM HILL RANCH'),
            ('Valley', 'BORDEN HILLS'),
            ('Valley', 'COWELL RANCH'),
            ('Valley', 'LIBERTY LODI'),
            ('Valley', 'LIVINGSTON RANCHES'),
            ('Valley', 'VALLEY OAK'),
            ('Southern', 'BRIDLEWOOD VYD'),
            ('Southern', 'EDNA VALLEY'),
            ('Southern', 'SUNNYBROOK RANCH')]
        self.expected_location = [('Southern', 'EDNA VALLEY', '[-120.606247480242, 35.2145817938914]')]
        self.expected_weather = {'coordinates': '[-120.606247480242, 35.2145817938914]',
            'name': 'EDNA VALLEY',
            'region': 'Southern',
            'current': {'clouds': 40,
                'dew_point': 275.99,
                'dt': 1646318698,
                'feels_like': 278.41,
                'humidity': 65,
                'pressure': 1014,
                'sunrise': 1646306882,
                'sunset': 1646347929,
                'temp': 282.21,
                'uvi': 2.55,
                'visibility': 10000,
                'weather': [{'description': 'scattered clouds',
                    'icon': '03d',
                    'id': 802,
                    'main': 'Clouds'}],
                'wind_deg': 360,
                'wind_gust': 13.89,
                'wind_speed': 8.75}}

    def test_regions(self):
        result = regions()
        self.assertEqual(result, self.expected_regions)

    def test_region(self):
        result = region("Valley")
        self.assertEqual(result, self.expected_region)

    def test_region_case_insensitive(self):
        result = region("VaLLeY")
        self.assertEqual(result, self.expected_region)

    def test_locations(self):
        result = locations()
        self.assertEqual(result, self.expected_locations)

    def test_location(self):
        result = location("EDNA VALLEY")
        self.assertEqual(result, self.expected_location)

    def test_location_case_insensitive(self):
        result = location("EdnA VaLLeY")
        self.assertEqual(result, self.expected_location)

    def test_weather(self):
        self.maxDiff = None
        result = weather("EDNA VALLEY")
        self.assertEqual(result, self.expected_weather)

    def test_weather_case_insensitive(self):
        self.maxDiff = None
        result = weather("EdnA VaLLeY")
        self.assertEqual(result, self.expected_weather)

if __name__ == '__main__':
        unittest.main()
