import unittest

#  Given an integer year, determine whether it is a leap year.
#  
#  A year is a leap year if it satisfies the following rules:
#  
#  The year is evenly divisible by 4, and
#  The year is not evenly divisible by 100, unless
#  The year is evenly divisible by 400.

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def is_leap_year(year):
    logging.debug(f'start of is_leap_year {year=}')
    return  (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0


class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(is_leap_year(2024) , True)
        self.assertEqual(is_leap_year(2023) , False)
        self.assertEqual(is_leap_year(2100) , False)
        self.assertEqual(is_leap_year(2000) , True)
        self.assertEqual(is_leap_year(1999) , False)
        self.assertEqual(is_leap_year(2040) , True)
        self.assertEqual(is_leap_year(2026) , False)

if __name__ == '__main__':

    unittest.main(verbosity=2)


