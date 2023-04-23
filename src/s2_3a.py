import json
import re

if __name__ == '__main__':
    persons = []
    with open("../docs/Personen.txt", "r") as input_file:
        for index, line in enumerate(input_file):
            try:
                info = line.strip().replace("\"", "").split(",")
                full_name = info[0].split(" ")
                last_name = full_name.pop(-1)
                title = "".join(re.findall("(Dr.|Dipl.|-?Ing.|Prof.|Univ.)\s*", full_name.pop(0))) if re.match("(Dr.|Dipl.|-?Ing.|Prof.|Univ.)\s*", full_name[0]) else None
                first_name = full_name.pop(0)
                middle_name = " ".join(full_name)
                birthdate = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", info[3]).strip()
                street_name = "".join(re.findall("\D", info[1])).strip()
                street_number = "".join(re.findall(r"\b\d{1,5}\b", info[1])).strip()
                postal_code = "".join(re.findall("\d{5}", info[2])).strip()
                residence = "".join(re.findall("\D", info[2])).strip()
                phone_number = "".join(re.findall(r"\+*[(0)|\d{5}]*[\s\d]+", info[4])).strip()
                person = {
                    "Index": index, "Titel": [None if title == "" else title],
                    "Vorname": [first_name], "Zweitname": [None if middle_name == " " else middle_name], "Nachname": [last_name],
                    "Geburtsdatum": [birthdate], "Telefon": [phone_number],
                    "Straße": [street_name], "Hausnummer": [street_number], "PLZ": [postal_code], "Wohnort": [residence]
                }
                persons.append(person)
            except IndexError:
                continue
    with open(r"Personen_Neu.json", "w") as output_file:
        json.dump(persons, output_file, indent=1, ensure_ascii=False)
