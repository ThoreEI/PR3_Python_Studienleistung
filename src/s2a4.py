import re


def normalize(telephone_number: str) -> str:
    pattern = re.compile(r"""
         ^(?P<country_code>\+?1?)[ ,.-]?
          (?P<phone_prefix>(\(?([2-9][0-8]\d)\))|([2-9][0-8])\d)[ ,.-]?
          (?P<exchange_code>\d{3})[ ,.-]?
          (?P<phone_extension>[2-9]\d{3})?\.?$
        """, re.VERBOSE)
    matches = pattern.match(telephone_number)
    if not matches:
        raise ValueError("Invalid phone number.")
    country_code = 1
    phone_prefix, exchange_code, phone_extension = \
        [re.sub(r'\D', '', match) for match in matches.group("phone_prefix", "exchange_code", "phone_extension")]
    return f'{country_code}-{phone_prefix}-{exchange_code}-{phone_extension}'


if __name__ == '__main__':
    for phone_number in ["+1 223-456-7890", "1-223-456-7890", "+1 223 456-7890", "(223)456-7890", "1 223 456 7890", "223.456.7890."]:
        print(normalize(phone_number))
