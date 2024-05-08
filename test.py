import unittest
from time_calculator import add_time

class TestAddTime(unittest.TestCase):
    def test_case_1(self):
        # Test case 1: Calling add_time('3:30 PM', '2:12') should return '5:42 PM'
        self.assertEqual(add_time('3:30 PM', '2:12'), '5:42 PM')

    def test_case_2(self):
        # Test case 2: Calling add_time('11:55 AM', '3:12') should return '3:07 PM'
        self.assertEqual(add_time('11:55 AM', '3:12'), '3:07 PM')

    def test_case_3(self):
        # Test case 3: Expected time to end with '(next day)' when it is the next day
        self.assertTrue(add_time('11:59 PM', '24:05').endswith('(next day)'))

    def test_case_4(self):
        # Test case 4: Expected period to change from AM to PM at 12:00
        self.assertTrue('AM' in add_time('11:59 AM', '0:02'))

    def test_case_5(self):
        # Test case 5: Calling add_time('2:59 AM', '24:00') should return '2:59 AM (next day)'
        self.assertEqual(add_time('2:59 AM', '24:00'), '2:59 AM (next day)')

    def test_case_6(self):
        # Test case 6: Calling add_time('11:59 PM', '24:05') should return '12:04 AM (2 days later)'
        self.assertEqual(add_time('11:59 PM', '24:05'), '12:04 AM (2 days later)')

    def test_case_7(self):
        # Test case 7: Calling add_time('8:16 PM', '466:02') should return '6:18 AM (20 days later)'
        self.assertEqual(add_time('8:16 PM', '466:02'), '6:18 AM (20 days later)')

    def test_case_8(self):
        # Test case 8: Expected adding 0:00 to return the initial time
        self.assertEqual(add_time('3:30 PM', '0:00'), '3:30 PM')

    def test_case_9(self):
        # Test case 9: Calling add_time('3:30 PM', '2:12', 'Monday') should return '5:42 PM, Monday'
        self.assertEqual(add_time('3:30 PM', '2:12', 'Monday'), '5:42 PM, Monday')

    def test_case_10(self):
        # Test case 10: Calling add_time('2:59 AM', '24:00', 'saturDay') should return '2:59 AM, Sunday (next day)'
        self.assertEqual(add_time('2:59 AM', '24:00', 'saturDay'), '2:59 AM, Sunday (next day)')

    def test_case_11(self):
        # Test case 11: Calling add_time('11:59 PM', '24:05', 'Wednesday') should return '12:04 AM, Friday (2 days later)'
        self.assertEqual(add_time('11:59 PM', '24:05', 'Wednesday'), '12:04 AM, Friday (2 days later)')

    def test_case_12(self):
        # Test case 12: Calling add_time('8:16 PM', '466:02', 'tuesday') should return '6:18 AM, Monday (20 days later)'
        self.assertEqual(add_time('8:16 PM', '466:02', 'tuesday'), '6:18 AM, Monday (20 days later)')

if __name__ == '__main__':
    unittest.main()
