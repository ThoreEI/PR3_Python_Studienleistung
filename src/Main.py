import regex as regex


class Person:
    titles_name: str
    first_name: str
    last_name: str
    street: str
    number: int
    postal_code: str
    residence: str


if __name__ == '__main__':
    with open("../docs/Personen.txt", "r") as input_file:
        personal_data = input_file.readlines()
    input_file.close()
    for read_line in personal_data:
        personal_data = regex.split(",", read_line)
        full_name = regex.split("\s", personal_data[0])
        street_and_number = regex.split, personal_data[1]  # adresse immer 2 Kommata
        postal_code_and_residence = personal_data[2]
        print(street_and_number)
        print(postal_code_and_residence)
