import unittest
from s2_a4_a import normalize

test_numbers = ["+1 223-456-7890", "1-223-456-7890", "+1 223 456-7890", "(223) 456-7890", "1 223 456 7890",
                "223.456.7890", "1-989-111-2222"]
expected_numbers = ["1-223-456-7890", "1-223-456-7890", "1-223-456-7890", "1-223-456-7890", "1-223-456-7890",
                    "1-223-456-7890", "1-989-111-2222"]


class TestNormalize(unittest.TestCase):
    def test_valid_numbers(self):
        for i in range(len(test_numbers)):
            with self.subTest(number=test_numbers[i]):
                self.assertEqual(normalize(test_numbers[i]), expected_numbers[i])

    def test_raise_value_error(self):
        for i in range(len(test_numbers)):
            with self.subTest(number=test_numbers[i]):
                self.assertRaises(ValueError, normalize, "1-111-111-1111")

    def test_invalid_prefix(self):
        for i in range(len(test_numbers)):
            with self.subTest(number=test_numbers[i]):
                self.assertRaises(ValueError, normalize, "1-911-111-1111")


    #
    # def test_number_array(self):
    #     for i in range(0, len(self.numbers) - 1):
    #         self.assertEqual(num_parser.parse_number(self.numbers[i]), '1-223-456-7890')
    #
    # def test_to_short_number(self):
    #     with self.assertRaises(num_parser.ValueError):
    #         num_parser.parse_number("1-223-456-789")
    #
    # def test_to_long_number(self):
    #     with self.assertRaises(num_parser.ValueError):
    #         num_parser.parse_number("1-223-456-78999")
    #
    # def test_false_prefix(self):
    #     with self.assertRaises(num_parser.ValueError):
    #         num_parser.parse_number("+2 223-456-7899")
    #
    # def test_false_first_ortsvorwahl(self):
    #     with self.assertRaises(num_parser.ValueError):
    #         num_parser.parse_number("+1 123-456-7899")
    #
    # def test_false_second_ortsvorwahl(self):
    #     with self.assertRaises(num_parser.ValueError):
    #         num_parser.parse_number("+1 193-456-7899")
