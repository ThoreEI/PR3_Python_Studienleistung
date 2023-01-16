import json
import re

if __name__ == '__main__':
    with open("../docs/Personen.txt", "r") as input_file:
        personal_data = input_file.readlines()
    input_file.close()

    list_of_persons = [None] * len(personal_data)
    index = 1
    for read_line in personal_data:
        try:
            personal_data = re.split(",", read_line)
            full_name = re.split("\s", personal_data[0])
            last_name = full_name.pop(-1)
            title = second_name = ""
            while re.match('Prof\.|Dr\.|Univ\.|Ing\.|Dipl\.', full_name[0]):
                title += full_name.pop(0)
            title = None if title == "" else title
            first_name = full_name.pop(0)
            while len(full_name) > 0:
                second_name = full_name.pop(0)
            second_name = None if second_name == "" else second_name

            street_and_number = personal_data[1]
            street_name = "".join(re.findall("\D", street_and_number)).replace("\"", "")
            street_number = "".join(re.findall(r"\b\d{1,4}\b", street_and_number))

            postal_code_and_residence = personal_data[2]
            postal_code = "".join(re.findall("\d{5}", postal_code_and_residence))
            residence = "".join(re.findall("\D", postal_code_and_residence)).replace("\"", "")

            birthdate = "".join(personal_data[3]).replace("-", ".")
            phone_number = personal_data[4].replace("\n", "")
            person = {
                "Index": index,
                "Titel": [title],
                "Vorname": [first_name],
                "Zweitname": [second_name],
                "Nachname": [last_name],
                "Strasse": [street_name],
                "Hausnummer": [street_number],
                "PLZ": [postal_code],
                "Wohnort": [residence],
                "Geburtsdatum": [birthdate]
            }
            list_of_persons[index - 1] = person
            index += 1
        except IndexError:
            continue
    with open(r"Personen_Neu.json", "w") as output_file:
        json.dump(list_of_persons, output_file, indent=1, ensure_ascii=False)
