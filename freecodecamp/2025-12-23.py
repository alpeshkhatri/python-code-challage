import unittest

# Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.
# 
# For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):
# 
# "fw:"
# "fwd:"
# "re:"
# Return the total number of occurrences of these markers.

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def email_chain_count(subject):
    logging.debug("starting email_chain_count")
    temp = subject.lower().split(":")
    temp = [t.strip() for t in temp]
    c = temp.count("fw") + temp.count("fwd") + temp.count("re")
    logging.debug(f"""{ temp.count("re") }""")
    logging.debug(f"{temp=} {c=}")
    return c

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(email_chain_count("Re: Meeting Notes") , 1)
        self.assertEqual(email_chain_count("Meeting Notes") , 0)
        self.assertEqual(email_chain_count("Re: re: RE: rE: Meeting Notes") , 4)
        self.assertEqual(email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes") , 5)
        self.assertEqual(email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary") , 23)

if __name__ == '__main__':

    unittest.main(verbosity=2)


