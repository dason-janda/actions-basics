import io
import unittest
from contextlib import redirect_stdout

from addition import addition, main


class TestAddition(unittest.TestCase):

    def test_adds_positive_numbers(self):
        self.assertEqual(addition(2, 3), 5)

    def test_adds_large_numbers(self):
        self.assertEqual(addition(328749, 928938), 1257687)

    def test_adds_negative_numbers(self):
        self.assertEqual(addition(-4, -6), -10)
        self.assertEqual(addition(-4, 10), 6)

    def test_adds_zero(self):
        self.assertEqual(addition(0, 7), 7)

    def test_adds_floats(self):
        self.assertAlmostEqual(addition(0.1, 0.2), 0.3)


class TestMainOutput(unittest.TestCase):

    def get_main_output(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            main()
        return buffer.getvalue()

    def test_print_format(self):
        output = self.get_main_output()
        # "The sum of <int> and <int> is <int>"
        self.assertRegex(output, r"^The sum of -?\d+ and -?\d+ is -?\d+\n$")

    def test_prints_one_line(self):
        output = self.get_main_output()
        self.assertEqual(len(output.splitlines()), 1)


if __name__ == '__main__':
    unittest.main()
