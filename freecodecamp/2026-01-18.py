import unittest

# Free Shipping
# Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.
#
# The given array will contain items from the list below:
#
# Item	Price
# "shirt"	34.25
# "jeans"	48.50
# "shoes"	75.00
# "hat"	19.95
# "socks"	15.00
# "jacket"	109.95
#

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def gets_free_shipping(cart, minimum):
    logging.debug("start of gets_free_shipping")
    price_map = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95,
    }
    total_price = 0
    for item in cart:
        total_price += price_map[item]
    return total_price >= minimum


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(gets_free_shipping(["shoes"], 50), True)
        self.assertEqual(gets_free_shipping(["hat", "socks"], 50), False)
        self.assertEqual(gets_free_shipping(["jeans", "shirt", "jacket"], 75), True)
        self.assertEqual(gets_free_shipping(["socks", "socks", "hat"], 75), False)
        self.assertEqual(
            gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100), True
        )
        self.assertEqual(
            gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200),
            False,
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
