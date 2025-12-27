import unittest

# Given a positive integer, return the sum of all its divisors.
# 
# A divisor is any integer that divides the number evenly (the remainder is 0).
# Only count each divisor once.
# For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12.


import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def sum_divisors(n):
    logging.debug('start of function')
    divisors = [1,n]
    cur = 2
    end = n
    while cur < end :
        t = n/cur
        if t.is_integer() :
            t = int(t)
            divisors.extend([cur,t])
            end = t
        cur = cur + 1 
        logging.debug(f"{cur=} {end=} {n=} {divisors=}")
    return sum(divisors)

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(sum_divisors(6) , 12)
        self.assertEqual(sum_divisors(13) , 14)
        self.assertEqual(sum_divisors(28) , 56)
        self.assertEqual(sum_divisors(84) , 224)
        self.assertEqual(sum_divisors(549) , 806)
        self.assertEqual(sum_divisors(9348) , 23520)

if __name__ == '__main__':
    unittest.main(verbosity=2)


