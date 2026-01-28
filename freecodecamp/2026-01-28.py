import unittest

# Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional array. Retain the original order of the items in the arrays.


import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def flatten(args):
    logging.debug(f"start of flatten {args=}")
    ret = []
    for item in args :
        if isinstance(item, list):
            ret.extend(flatten(item))
        else:
            ret.append(item)
    logging.debug(f"{ret=}")
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(flatten([1, [2, 3], 4]), [1, 2, 3, 4])
        self.assertEqual(flatten([5, [4, [3, 2]], 1]), [5, 4, 3, 2, 1])
        self.assertEqual(flatten(["A", [[[["B"]]]], "C"]), ["A", "B", "C"])
        self.assertEqual(
            flatten(
                [
                    ["L", "M", "N"],
                    ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]],
                    "V",
                    ["W", ["X", ["Y", ["Z"]]]],
                ]
            ),
            ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        )
        self.assertEqual(
            flatten(
                [
                    ["red", ["blue", ["green", ["yellow", ["purple"]]]]],
                    "orange",
                    ["pink", ["brown"]],
                ]
            ),
            ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"],
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
