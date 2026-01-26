import unittest

# Scaled Image
# Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.
#
# The input string is in the format "WxH". For example, "800x600".
# The scale is a number to multiply the width and height by.
# Return the scaled dimensions in the same "WxH" format.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def scale_image(args,scale):
    logging.debug(f"start of scale_image {args=}")
    w,h = args.split('x')
    w,h = int(w),int(h)
    return f"{int(w*scale)}x{int(h*scale)}"


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(scale_image("800x600", 2), "1600x1200")
        self.assertEqual(scale_image("100x100", 10), "1000x1000")
        self.assertEqual(scale_image("1024x768", 0.5), "512x384")
        self.assertEqual(scale_image("300x200", 1.5), "450x300")


if __name__ == "__main__":

    unittest.main(verbosity=2)
