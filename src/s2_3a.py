import json
import re

if __name__ == '__main__':
    persons = []
    with open("../docs/Personen.txt", "r", encoding="utf-8") as input_file:
        for index, line in enumerate(input_file):
            try:
                info = line.strip().replace("\"", "").split(",")
                full_name = info[0].split(" ")
                last_name = full_name.pop(-1)
                title = "".join(re.findall("(Dr.|Dipl.|-?Ing.|-?Prof.|Univ.)\s*", full_name.pop(0))) \
                    if re.match("(Dr.|Dipl.|-?Ing.|-?Prof.|Univ.)\s*", full_name[0]) else None
                first_name = full_name.pop(0)
                middle_name = " ".join(full_name[1:]) if len(full_name) > 1 else None
                birthdate = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", info[3]).strip()
                street_name = re.sub(r"\d+", "", info[1]).strip()
                street_number = re.sub(r"\D+", "", info[1]).strip()
                postal_code = re.sub(r"\D+", "", info[2]).strip()
                residence = re.sub(r"\d+", "", info[2]).strip()
                persons.append({"Index": index,
                                "Titel": [None if title == "" else title],
                                "Vorname": [first_name],
                                "Zweitname": [None if middle_name == " " else middle_name],
                                "Nachname": [last_name],
                                "Geburtsdatum": [birthdate],
                                "Straße": [street_name],
                                "Hausnummer": [street_number],
                                "PLZ": [postal_code],
                                "Wohnort": [residence]})
            except IndexError:
                continue
    with open(r"../docs/Personen_Neu.json", "w") as output_file:
        json.dump(persons, output_file, indent=2, ensure_ascii=False)
