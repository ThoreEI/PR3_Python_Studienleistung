import re
class ValueError(Exception):
    def __init__(self):
        super().__init__("Ungültige Telefonnummer")

def parseNumber( number):
    number = number if not re.search('^[+][1] ', number) else number[3:]
    number = number if not re.search('^[1][ ./-]', number) else number[2:]

    if re.search("([2-9][0-8]\d|[(][2-9][0-8]\d[)])[ ./-]\d{3}[ ./-]\d{4}", number) and (len(number) == 12 or len(number) == 14):
        return "1-" + number[1:4] + "-" + number[6:9] + "-" + number[10:] if re.search('^[(]', number) else "1-" + number[0:3] + "-" + number[4:7] + "-" + number[8:]
    else:
        raise ValueError()

if __name__ == "__main__":
    newNumbers = []
    numbers = ["+1 223-456 7890", "1 223-456-7890", "+1 223 456-7890", "(223) 456-7890", "1 223456 7890", "223.456.7890"]

    counter = 0
    for num in numbers:
        try:
            newNumbers.append(parseNumber(num))
        except ValueError:
            print("Ungültige Nummer an Positon array Postion: " + str(counter))
        counter += 1

    print(newNumbers)
