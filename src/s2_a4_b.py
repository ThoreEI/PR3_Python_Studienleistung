import unittest
import re

class ValueError(Exception):
    def __init__(self, message="Salary is not in (5000, 15000) range"):
        self.message = message
        super().__init__(self.message)

class NumberNormer:
    def __init__(self):
        self.__ortsvorwahl = ""
        self.__amstkennung = ""
        self.__vorwahl = ""

    def parseNumber(self, number):
        print("1: " +number)
        if re.search('[+][1][ ./-]([2-9][0-8][0-9]|[(][2-9][0-8][0-9][)])[-. ][0-9]{3}[-. ][0-9]{4}', number):
            self.checkOrtsVorwahl(number[3:])
        elif re.search('[1][ ./-]([2-9][0-8][0-9]|[(][2-9][0-8][0-9][)])[-. ][0-9]{3}[-. ][0-9]{4}', number):
            self.checkOrtsVorwahl(number[2:])
        elif re.search('([2-9][0-8][0-9]|[(][2-9][0-8][0-9][)])[-. ][0-9]{3}[-. ][0-9]{4}', number):
            self.checkOrtsVorwahl(number)
        else:
            raise ValueError()

        return "1-" + self.__ortsvorwahl + "-" + self.__amstkennung + "-" + self.__vorwahl


    def checkOrtsVorwahl(self, number):
        print("2: " + number)
        if re.search('[(][2-9][0-8][0-9][)][ ./-][0-9]{3}[ ./-][0-9]{4}', number):
            self.__ortsvorwahl = number[1:4]
            self.checkAmtskennung(number[6:])
        elif re.search('[2-9][0-8][0-9][ ./-][0-9]{3}[ ./-][0-9]{4}', number):
            self.__ortsvorwahl = number[0:3]
            self.checkAmtskennung(number[4:])
        else:
            raise ValueError()

    def checkAmtskennung(self, number):
        print("3: " +number)
        if re.search('[0-9]{3}[ ./-][0-9]{4}', number):
            self.__amstkennung = number[0:3]
            self.checkVorwahl(number[4:])
        else:
            raise ValueError()

    def checkVorwahl(self, number):
        print("4: " +number)
        if re.search('[0-9]{4}', number):
            self.__vorwahl = number[0:4]
        else:
            raise ValueError()


class testNumbers(unittest.TestCase):

    numbers = ["+1 223-456 7890", "1-223-456-7890", "+1 223 456-7890", "(223) 456-7890", "1 223 456 7890", "223.456.7890", "1-989-111-2222"]
    res_numbers = ['1-223-456-7890', '1-223-456-7890', '1-223-456-7890', '1-223-456-7890', '1-223-456-7890', '1-223-456-7890', '1-989-111-2222']

    nm = NumberNormer()

    def test_number_arrays(self):

        for i in range(0, len(self.numbers)-1):
            self.assertEqual(self.nm.parseNumber(self.numbers[i]), self.res_numbers[i])


    def test_with_falseNumber(self):

        with self.assertRaises(ValueError):
            self.nm.parseNumber("12223324444")