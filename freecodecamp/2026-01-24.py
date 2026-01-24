import unittest

# Bingo! Letter
# Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:
#
# Letter	Number Range
# "B"	1-15
# "I"	16-30
# "N"	31-45
# "G"	46-60
# "O"	61-75

def get_bingo_letter(number):
    """ALterNative way. Returns the BINGO letter for a number between 1 and 75."""
    if not 1 <= number <= 75:
        raise ValueError("Number must be between 1 and 75")

    ranges = {
        range(1, 16): "B",
        range(16, 31): "I",
        range(31, 46): "N",
        range(46, 61): "G",
        range(61, 76): "O",
    }

    for r, letter in ranges.items():
        if number in r:
            return letter


import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")



def get_bingo_letter(args):
    logging.debug("start of get_bingo_letter")
    if args in range(1, 15 + 1):
        return "B"
    if args in range(16, 30 + 1):
        return "I"
    if args in range(31, 45 + 1):
        return "N"
    if args in range(46, 60 + 1):
        return "G"
    if args in range(61, 75 + 1):
        return "O"

class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(get_bingo_letter(75), "O")
        self.assertEqual(get_bingo_letter(54), "G")
        self.assertEqual(get_bingo_letter(25), "I")
        self.assertEqual(get_bingo_letter(38), "N")
        self.assertEqual(get_bingo_letter(11), "B")


if __name__ == "__main__":

    unittest.main(verbosity=2)
