import unittest

# FizzBuzz Mini
# Given an integer, return a string based on the following rules:
#
# If the number is divisible by 3, return "Fizz".
# If the number is divisible by 5, return "Buzz".
# If the number is divisible by both 3 and 5, return "FizzBuzz".
# Otherwise, return the given number as a string.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def fizz_buzz_mini(args: int) -> str:
    logging.debug(f"start of fizz_buzz_mini {args=}")
    ret = ""
    ret += "Fizz" if (args % 3) == 0 else ""
    ret += "Buzz" if (args % 5) == 0 else ""
    ret = str(args) if ret == "" else ret
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(fizz_buzz_mini(3), "Fizz")
        self.assertEqual(fizz_buzz_mini(4), "4")
        self.assertEqual(fizz_buzz_mini(35), "Buzz")
        self.assertEqual(fizz_buzz_mini(75), "FizzBuzz")
        self.assertEqual(fizz_buzz_mini(98), "98")


if __name__ == "__main__":

    unittest.main(verbosity=2)
