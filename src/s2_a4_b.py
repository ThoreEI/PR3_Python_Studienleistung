import unittest
import re
import s2_a4_a as numParser

class testNumbers(unittest.TestCase):

    numbers = ["+1 223-456 7890", "1-223-456-7890", "+1 223 456-7890", "(223) 456-7890", "1 223 456 7890", "223.456.7890"]

    def test_number_array(self):

        for i in range(0, len(self.numbers)-1):
            self.assertEqual(numParser.parseNumber(self.numbers[i]), '1-223-456-7890')


    def test_to_short_number(self):
        with self.assertRaises(numParser.ValueError):
            numParser.parseNumber("1-223-456-789")

    def test_to_long_number(self):
        with self.assertRaises(numParser.ValueError):
            numParser.parseNumber("1-223-456-78999")

    def test_false_prefix(self):
        with self.assertRaises(numParser.ValueError):
            numParser.parseNumber("+2 223-456-7899")

    def test_false_first_ortsvorwhal(self):
        with self.assertRaises(numParser.ValueError):
            numParser.parseNumber("+1 123-456-7899")

    def test_false_second_ortsvorwhal(self):
        with self.assertRaises(numParser.ValueError):
            numParser.parseNumber("+1 193-456-7899")
