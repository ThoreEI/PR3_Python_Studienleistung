# import pprint
# import re
# import json
#
# if __name__ == '__main__':
#     with open("docs/Personen.txt", "r", encoding="utf-8") as input_file:
#         data = input_file.read().splitlines()
#         persons = []
#         for index, line in enumerate(data):
#             if index == 0:
#                 continue
#
#             match = re.match(r'^(?P<name>(?P<title>(?:Dr\.|Dipl\.|-?Ing\.|Prof\.|Univ\.)*\s)?)(?P<first_name>[A-Z][a-z]+(-?[A-Z][a-z]+)?)\s(?P<middle_name>[A-Z][a-z]+(-[A-Z][a-z]+)?)?\s(?P<last_name>[A-Z][a-z]+(-[A-Z][a-z]+)?),(?P<address>.+?)(,\s*(?P<postal_code>\d{5}))?(,\s*(?P<phone>.+))?,(?P<birthdate>\d{4}-\d{2}-\d{2})$',line)
#             info = line.replace("\"", "").split(",")
#             name = info.pop(0).strip().split(" ")
#             phone_number = info.pop().strip()
#             if not re.match(r"\+*[(0)|\d{5}]*[\s\d]+", phone_number):
#                 raise ValueError("Invalid phone number.")
#             birthdate = info.pop().strip()
#             if not re.match(r"\d{4}-[\d{2}\-]{2}", birthdate):
#                 raise ValueError("Invalid birthdate.")
#
#             # address = " ".join(info)  # remaining information
#             # if not name_match:
#             #     print(name_match)
#             # titles = regex.search(r'^(Dr\.|Dipl\.|-*Ing\.|Prof\.|Univ\.)*$', name)
#             # print(name_match)
#             # # name = re.sub(titles, "", name).strip()
#             # first_name = name.pop(0)
#             # last_name = name.pop() if name else None
#             # middle_name = "".join(name)  # remaining name after removing first/last name
#             #
#             # address_match = re.match(
#             #     r"^(?P<street>[\w\s\-\.]+)\s(?P<street_number>\d+)\s(?P<postalcode>\d{5})\s(?P<residence>[\w\s-]+).*$",
#             #     address)
#             # if not address_match:
#             #     raise ValueError("Invalid address formatting.")
#             #
#             # street = address_match.group("street")
#             # street_number = address_match.group("street_number")
#             # postalcode = address_match.group("postalcode")
#             # residence = address_match.group("residence")
#             # #
#             # # street = address.pop(0)
#             # # street_number = address.pop(0)
#             # # postal_code = address.pop(0)
#             # # residence = address.pop(0)
#             # # while address:
#             # #     residence += address.pop()
#             # # print(f'''
#             # # {residence}
#             # # ''')
#             person = {
#                 'Index': index + 1,
#                 'Titel': [titles] if titles else [None],
#                 'Vorname': [first_name] if first_name else [None],
#                 'Zweitname': [middle_name] if middle_name else [None],
#                 'Nachname': [last_name] if last_name else [None],
#                 'Geburtsdatum': [birthdate] if birthdate else [None],
#                 'Straße': [street] if street else [None],
#                 'Hausnummer': [street_number] if street_number else [None],
#                 'PLZ': [postalcode] if postalcode else [None],
#                 'Wohnort': [residence] if residence else [None]
#             }
#             persons.append(person)
#     with open("PersonenNeu2.json", "w", encoding="utf-8") as output_file:
#         json.dump(persons, output_file, ensure_ascii=False, indent=4)
# # title = match.group("title")
# # first_name = match.group("first_name")
# # middle_name = match.group("middle_name")
# # last_name = match.group("last_name")
# # address = match.group("address")
# # birthdate = match.group("birthdate")
# # phone_number = match.group("phone")
# # print(f"{title}\n{first_name}\n{middle_name}\n{last_name}\n{address}\n{birthdate}\n{phone_number}\n\n")
