import unittest

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def myFunction(args):
    logging.debug(f"start of myFunction {args=}")
    return "ret"


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(myFunction("args"), "ret")


if __name__ == "__main__":

    unittest.main(verbosity=2)
