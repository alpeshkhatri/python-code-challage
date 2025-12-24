import unittest

def title_case(title : str):
    return ' '.join([x.capitalize() for x in title.split()])


class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")
        self.assertEqual(title_case("JAVASCRIPT AND PYTHON"), "Javascript And Python")
        self.assertEqual(title_case("AvOcAdO tOAst fOr brEAkfAst"), "Avocado Toast For Breakfast")

if __name__ == '__main__':
    unittest.main(verbosity=2)
