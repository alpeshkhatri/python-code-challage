import unittest

#  Given an integer, determine if it is a circular prime.
#  
#  A circular prime is an integer where all rotations of its digits are themselves prime.
#  
#  For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.
#  
import logging
from functools import cache
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

@cache
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Only check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # Skip even numbers
    return True

def get_rotation(n):
    ns = str(n)
    for i in range(len(ns)):
        r = ns[i:] + ns[:i]
        yield int(r)

def is_circular_prime(n):
    logging.debug('start of is_circular_prime')
    if not is_prime(n):
        return False
    for i in get_rotation(n):
        logging.debug(f'{i=}')
        if not is_prime(i):
            return False
    return True

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 

        self.assertEqual(is_circular_prime(197) , True)
        self.assertEqual(is_circular_prime(23) , False)
        self.assertEqual(is_circular_prime(13) , True)
        self.assertEqual(is_circular_prime(89) , False)
        self.assertEqual(is_circular_prime(1193) , True)

if __name__ == '__main__':

    unittest.main(verbosity=2)


