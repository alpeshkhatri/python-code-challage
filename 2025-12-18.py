import unittest

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def ret_X_O(start):
    if start == "O" :
         yield "O"
    while(True):
        yield "X"
        yield "O"

def create_board(dimensions):
    logging.debug('start myfunction')
    matrix = []
    logging.debug(dimensions)
    v = ret_X_O("X")
    count = 0
    for r in range(0,dimensions[0]) :
        row = []
        logging.debug(r % 2 == 1)
        for c in range(0,dimensions[1]):
            count += 1
            v1 = next(v)
            row.append(v1)
        matrix.append(row)
        if count % 2 ==  0 : # even
            v = ret_X_O(matrix[r][-1])
        count = 0

    logging.debug(matrix)
    return matrix

#-----------------

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(create_board([3, 3]), [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])
        self.assertEqual(create_board([1, 3]), [["X", "O", "X"]])
        self.assertEqual(create_board([6, 1]), [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]])
        self.assertEqual(create_board([2, 10]), [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]])
        self.assertEqual(create_board([5, 4]), [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]])
if __name__ == '__main__':
    unittest.main(verbosity=2)

