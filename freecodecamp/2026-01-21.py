import unittest

#  Markdown Inline Code Parser
#  Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.
#
#  Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.
#
#  Return the given string with all code blocks converted to HTML code tags.
#
#  For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".
#
#  Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

import logging
import re
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def parse_inline_code(args):
    logging.debug("start of parse_inline_code")
    logging.debug(f"{args=}")
    ret = re.sub(r'`([^`]+)`',r'<code>\1</code>',args)
    logging.debug(f'{ret=}')
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(
            parse_inline_code("Use `let` to declare the variable."),
            "Use <code>let</code> to declare the variable.",
        )
        self.assertEqual(
            parse_inline_code("Use `let` or `const` to declare a variable."),
            "Use <code>let</code> or <code>const</code> to declare a variable.",
        )
        self.assertEqual(
            parse_inline_code("Run `npm install` then `npm start`."),
            "Run <code>npm install</code> then <code>npm start</code>.",
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
