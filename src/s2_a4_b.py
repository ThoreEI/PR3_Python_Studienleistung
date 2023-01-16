import unittest
import s2_a4_a as num_parser


class TestNumbers(unittest.TestCase):
    numbers = ["+1 223-456 7890", "1-223-456-7890", "+1 223 456-7890", "(223) 456-7890", "1 223 456 7890", "223.456.7890"]

    def test_number_array(self):
        for i in range(0, len(self.numbers) - 1):
            self.assertEqual(num_parser.parse_number(self.numbers[i]), '1-223-456-7890')

    def test_to_short_number(self):
        with self.assertRaises(num_parser.ValueError):
            num_parser.parse_number("1-223-456-789")

    def test_to_long_number(self):
        with self.assertRaises(num_parser.ValueError):
            num_parser.parse_number("1-223-456-78999")

    def test_false_prefix(self):
        with self.assertRaises(num_parser.ValueError):
            num_parser.parse_number("+2 223-456-7899")

    def test_false_first_ortsvorwahl(self):
        with self.assertRaises(num_parser.ValueError):
            num_parser.parse_number("+1 123-456-7899")

    def test_false_second_ortsvorwahl(self):
        with self.assertRaises(num_parser.ValueError):
            num_parser.parse_number("+1 193-456-7899")
