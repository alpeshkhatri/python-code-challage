import unittest

# Odd or Even Day
# Given a timestamp (number of milliseconds since the Unix epoch), return:
#
# "odd" if the day of the month for that timestamp is odd.
# "even" if the day of the month for that timestamp is even.
# For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.


import logging
import datetime

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

def odd_or_even_day(args):
    logging.debug(f"start of odd_or_even_day {args=}")
    dt = datetime.datetime.fromtimestamp(args//1000, tz=datetime.timezone.utc)
    logging.debug(f"{dt=}")
    return "even" if ( dt.day % 2 ) == 0 else "odd"


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(odd_or_even_day(1769472000000), "odd")
        self.assertEqual(odd_or_even_day(1769444440000), "even")
        self.assertEqual(odd_or_even_day(6739456780000), "odd")
        self.assertEqual(odd_or_even_day(1), "odd")
        self.assertEqual(odd_or_even_day(86400000), "even")


if __name__ == "__main__":

    unittest.main(verbosity=2)
