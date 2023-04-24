import re


def normalize(number: str) -> str:
    pattern = re.compile(r"""
                 ^(?P<country_code>\+?1?)[ ,.-]?
                  (?P<phone_prefix>(\(?([2-9][0-8]\d)\))|([2-9][0-8])\d)[ ,.-]?
                  (?P<exchange_code>\d{3})[ ,.-]?
                  (?P<phone_extension>[2-9]\d{3})?\.?$
            """, re.VERBOSE)
    matches = pattern.match(number)
    if not matches:
        raise ValueError("Invalid phone number.")
    telephone_number = [re.sub(r"\D", "", match)
                        for match in matches.group("country_code", "phone_prefix", "exchange_code", "phone_extension")]
    print(telephone_number)
    return "-".join(telephone_number)
