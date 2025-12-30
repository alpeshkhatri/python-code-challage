from typing import List
import unittest

# Given the array of intergers return indices of the two number such that they add up to a specific target.

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Solution:
    def twoSum(self, nums: List[int], target: int) -> str :
        logging.debug("starting twoSum")
        map = {} # n, idx
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff],idx]
            map[n] = idx
        return 


class TestCodeChallege(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def tearDown(self):
        self.sol = None
    def test_twoSum(self): 
        self.assertEqual(self.sol.twoSum([1,2,3,4,5,6,7,8,9,0],10), [3,5])
        self.assertEqual(self.sol.twoSum([1,2,3,4,5,6,7,8,9,0],17), [7,8])

if __name__ == '__main__':
    unittest.main(verbosity=2)


