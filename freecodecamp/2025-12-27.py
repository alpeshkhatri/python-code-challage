import unittest

#  Rock, Paper, Scissors
#  Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.
#  
#  The input strings will always be "Rock", "Paper", or "Scissors".
#  "Rock" beats "Scissors".
#  "Paper" beats "Rock".
#  "Scissors" beats "Paper".
#  Return:
#  
#  "Player 1 wins" if Player 1 wins.
#  "Player 2 wins" if Player 2 wins.
#  "Tie" if both players choose the same option.
#  
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def rock_paper_scissors(player1, player2):
    logging.debug('start of function')
    options = ["Rock", "Paper", "Scissors"]
    p1idx = options.index(player1)
    p2idx = options.index(player2)
    diff_p1_p2 = p1idx - p2idx
    logging.debug(f"{player1=} {player2=} {p1idx=} {p2idx=} {diff_p1_p2=}")
    if diff_p1_p2 == 0  :
        return "Tie"
    elif diff_p1_p2 == 1 or diff_p1_p2 == -2:
        return "Player 1 wins"
    else:
        return "Player 2 wins"


class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(rock_paper_scissors("Rock", "Rock") , "Tie")
        self.assertEqual(rock_paper_scissors("Rock", "Paper") , "Player 2 wins")
        self.assertEqual(rock_paper_scissors("Scissors", "Paper") , "Player 1 wins")
        self.assertEqual(rock_paper_scissors("Rock", "Scissors") , "Player 1 wins")
        self.assertEqual(rock_paper_scissors("Scissors", "Scissors") , "Tie")
        self.assertEqual(rock_paper_scissors("Scissors", "Rock") , "Player 2 wins")

if __name__ == '__main__':

    unittest.main(verbosity=2)


