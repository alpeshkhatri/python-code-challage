import unittest
from typing import List


# Description

import logging
import collections

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        logging.debug("starting maxSlidingWindow")
        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # remove left value from window
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


class TestCodeChallenge(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tearDown(self):
        self.sol = None

    def test_maxSlidingWindow(self):
        self.assertEqual(
            self.sol.maxSlidingWindow([1, 2, -1, -3, 5, 3, 6, 7], 3), [2, 2, 5, 5, 6, 7]
        )
        self.assertEqual(self.sol.maxSlidingWindow([8, 7, 6, 9, 10], 2), [8, 7, 9, 10])


if __name__ == "__main__":
    unittest.main(verbosity=2)
