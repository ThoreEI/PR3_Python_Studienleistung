import re
import json


class FileReader:
    def __init__(self):
        self.__person_data = []
        self.__dictionary = {}
        self.load_persons()

    def load_persons(self):
        input_file = open("../docs/Personen.txt")
        for person_information in input_file:
            self.__person_data.append(person_information)

    def get_index(self):
        return len(self.__person_data)

    @property
    def get_persons(self):
        if len(self.__person_data) != 0:
            full_name = re.split(',', self.__person_data.pop(0))
            self.__set_titles(full_name)
            birthdate = self.__person_data.pop()
            self.__set_birthdate(birthdate)
            address = self.__person_data  # alles entfernt, Rest muss Adresse sein
            self.__set_address(address)
            return self.__dictionary

    def __set_titles(self, full_name):
        while re.match('"Prof."|"Dr.|"Univ."|"Ing."|"Dipl.', full_name[0]):  # if re.match("^[a-z.'-]{3}$", full_name):
            self.__dictionary["title"] += full_name.pop(0)
        self.__set_names(full_name)

    def __set_names(self, names):
        self.__dictionary["first_name"] = names[0]
        self.__dictionary["second_name"] = names[1] if len(names) == 3 else None
        self.__dictionary["last_name"] = names[-1]

    def __parse_and_check_address(self, address):
        # b)
        street_num = re.findall("[A-ZÄÖÜ][a-z]* \d{1,3}", address)
        plz_resident = re.findall("\d{5} [A-Z][a-z]*", address)

        if len(street_num) != 0 and len(plz_resident) != 0:
            street = re.findall("[A-ZÄÖÜ][a-z]*", street_num[0])
            num = re.findall("\d{1,3}", street_num[0])
            plz = re.findall("\d{5}", plz_resident[0])
            resident = re.findall("[A-Za-z]*", plz_resident[0])
            self.__set_address(street[0], num[0], plz[0], resident[0])
            return True
        return False

    def __set_address(self, address):
        self.__dictionary["street"] = address[0]
        self.__dictionary["number"] = address[1]
        #self.__dictionary["residence"] = address[3]
        # self.__dictionary["plz"] = address[2]
        # self.__dictionary["residence"] = address[3]

    def __set_birthdate(self, birthday):
        # c)
        n_date = "^(1[0-9][0-9][0-9]|20[012][0123])[.-/ ](0[1-9]|1[012])[.-/ ]([012][1-9]|3[01])"
        c_date = "^([012][1-9]|3[01])[.-/ ](0[1-9]|1[012])[.-/ ](1[0-9][0-9][0-9]|20[012][0123])"
        a_date = "^(0[1-9]|1[012])[.-/ ]([012][1-9]|3[01])[.-/ ](1[0-9][0-9][0-9]|20[012][0123])"

        date_array = re.split('[ /\-]', birthday)
        if re.search(n_date, birthday):  # 2001 08 01
            self.__create_german_datetime(date_array[2], date_array[1], date_array[0])
            return True
        elif re.search(c_date, birthday):  # 01 08 2001
            self.__create_german_datetime(date_array[0], date_array[1], date_array[2])
            return True
        elif re.search(a_date, birthday):  # 12 25 2001
            self.__create_german_datetime(date_array[1], date_array[0], date_array[2])
            return True
        return False

    def __create_german_datetime(self, day, month, year):
        self.__dictionary["Geburtstag"] = day + "." + month + "." + year


if __name__ == "__main__":
    personParser = FileReader()
    with open("../docs/PersonenNeu.json", "w") as outfile:
        person = personParser.get_persons
        outfile.write("[")
        while person is not None:
            json.dump(person, outfile)
            outfile.write(", ")
            person = personParser.get_persons
        outfile.write("]")
