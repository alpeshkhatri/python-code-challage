import unittest

#  Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.
#  
#  Mirror a line by reversing all of its characters, including spaces.
#  For example, given "* \n *\n* ", which logs to the console as:
#  
#  * 
#   *
#  * 
#  Return "*  *\n ** \n*  *", which logs to the console as:
#  
#  *  *
#   ** 
#  *  *
#  Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def generate_snowflake(crystals: str) -> str:
    logging.debug('start of function')
    ret: str = ""
    for line in crystals.splitlines() :
        ret += line + line[::-1] + "\n"
    return ret[:-1]

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(generate_snowflake("* \n *\n* ") , "*  *\n ** \n*  *")
        self.assertEqual(generate_snowflake("X=~") , "X=~~=X")
        self.assertEqual(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  ") , " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ")
        self.assertEqual(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *") , "*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *")
        self.assertEqual(generate_snowflake("*  -\n * -\n*  -") , "*  --  *\n * -- * \n*  --  *")

if __name__ == '__main__':

    unittest.main(verbosity=2)


