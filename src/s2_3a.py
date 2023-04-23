import json
import pprint
import re

if __name__ == '__main__':
    with open("../docs/Personen.txt", "r") as input_file:
        data = input_file.readlines()
    persons = []
    for index, line in enumerate(data):
        try:
            info = line.strip().replace("\"", "").split(",")
            name_parts = info[0].split(" ")
            last_name = name_parts.pop(-1)
            title = ""
            if re.match("(Dr.|Dipl.|-?Ing.|Prof.|Univ.)\s*", name_parts[0]):
                title = " ".join(re.findall("(Dr.|Dipl.|-?Ing.|Prof.|Univ.)\s*", name_parts.pop(0)))
            first_name = name_parts.pop(0)
            # middle_name = " ".join(re.findall(r"[A-Z][a-z]+(-?[A-Z][a-z]+)?\s", name_parts[0]))
            middle_name = ""
            while len(name_parts) > 0:
                middle_name += name_parts.pop(0)
            street_name = "".join(re.findall("\D", info[1]))
            street_number = "".join(re.findall(r"\b\d{1,5}\b", info[1]))
            postal_code = "".join(re.findall("\d{5}", info[2]))
            residence = "".join(re.findall("\D", info[2]))
            birthdate = "".join(info[3]).replace("-", ".")
            phone_number = info[4]
            person = {
                "Index": [index],
                "Titel": [None if title == "" else title],
                "Vorname": [first_name],
                "Zweitname": [None if middle_name == "" else middle_name],
                "Nachname": [last_name],
                "Strasse": [street_name],
                "Hausnummer": [street_number],
                "PLZ": [postal_code],
                "Wohnort": [residence],
                "Geburtsdatum": [birthdate],
                "Telefon": [phone_number]
            }
            persons.append(person)
        except IndexError:
            continue
        pprint.pp(persons)
    with open(r"Personen_Neu.json", "w") as output_file:
        json.dump(persons, output_file, indent=1, ensure_ascii=False)
