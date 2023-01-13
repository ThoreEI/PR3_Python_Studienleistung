import re


class ValueError(Exception):
    def __init__(self, message="Salary is not in (5000, 15000) range"):
        self.message = message
        super().__init__(self.message)


class NumberNormer:
    def __init__(self):
        self.__ortsvorwahl = ""
        self.__amtskennung = ""
        self.__vorwahl = ""

    def parse_number(self, number):
        print("1: " + number)
        if re.search('[+][1][ ./-]([2-9][0-8][0-9]|[(][2-9][0-8][0-9][)])[-. ][0-9]{3}[-. ][0-9]{4}', number):
            self.check_ortsvorwahl(number[3:])
        elif re.search('[1][ ./-]([2-9][0-8][0-9]|[(][2-9][0-8][0-9][)])[-. ][0-9]{3}[-. ][0-9]{4}', number):
            self.check_ortsvorwahl(number[2:])
        elif re.search('([2-9][0-8][0-9]|[(][2-9][0-8][0-9][)])[-. ][0-9]{3}[-. ][0-9]{4}', number):
            self.check_ortsvorwahl(number)
        else:
            raise ValueError()

        return "1-" + self.__ortsvorwahl + "-" + self.__amtskennung + "-" + self.__vorwahl

    def check_ortsvorwahl(self, number):
        print("2: " + number)
        if re.search('[(][2-9][0-8][0-9][)][ ./-][0-9]{3}[ ./-][0-9]{4}', number):
            self.__ortsvorwahl = number[1:4]
            self.check_amtskennung(number[6:])
        elif re.search('[2-9][0-8][0-9][ ./-][0-9]{3}[ ./-][0-9]{4}', number):
            self.__ortsvorwahl = number[0:3]
            self.check_amtskennung(number[4:])
        else:
            raise ValueError()

    def check_amtskennung(self, number):
        print("3: " + number)
        if re.search('[0-9]{3}[ ./-][0-9]{4}', number):
            self.__amtskennung = number[0:3]
            self.check_vorwahl(number[4:])
        else:
            raise ValueError()

    def check_vorwahl(self, number):
        print("4: " + number)
        if re.search('[0-9]{4}', number):
            self.__vorwahl = number[0:4]
        else:
            raise ValueError()


if __name__ == "__main__":
    nm = NumberNormer()
    newNumbers = []
    numbers = ["1 222-456-7890", "1-223-456 7890", "+1 223 456-7890", "(223) 457-7890", "223 456 7890", "223.456.7890"]
    test_numbers = ["+1 223-456 7890",
                    "1-223-456-7890",
                    "+1 223 456-7890",
                    "(223) 456-7890",
                    "1 223 456 7890",
                    "223.456.7890",
                    "1-989-111-2222"]

    for num in test_numbers:
        newNumbers.append(nm.parse_number(num))

    print(newNumbers)
