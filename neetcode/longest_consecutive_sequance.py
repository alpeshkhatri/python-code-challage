import unittest
from typing import List


# Given an unsorted array of integers find the length of the longest consecutive elements in the sequence.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class Solution:
    def longestConsecutive(self, args: List[int]) -> int:
        logging.debug("starting longestConsecutive")
        numSet = set(args)
        longest = 0
        for n in args:
            if (n - 1) not in numSet:  # check if its the start of a sequence
                length = 0
                while (n + length) in numSet:  # check end of the sequence
                    length += 1
                longest = max(length, longest)
        return longest


class TestCodeChallenge(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tearDown(self):
        self.sol = None

    def test_longestConsecutive(self):
        self.assertEqual(self.sol.longestConsecutive([100, 4, 200, 1, 2, 3]), 4)
        self.assertEqual(self.sol.longestConsecutive([100, 4, 200, 1, 2, 3, 5]), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
