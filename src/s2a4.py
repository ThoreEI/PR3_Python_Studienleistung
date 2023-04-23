import re


def normalize(phone_number: str) -> str:
    pattern = re.compile(r"""
         ^(?P<country_code>\+?1?)[ ,.-]?
          (?P<phone_prefix>\(?([2-9][0-8]\d)\)?|[2-9][0-8]\d)[ ,.-]?
          (?P<exchange_code>\d{3})[ ,.-]?
          (?P<phone_extension>[2-9]\d{3})?\.?$
        """, re.VERBOSE)
    match = pattern.match(phone_number)
    if match:
        country_code = match.group("country_code")
        phone_prefix = match.group("phone_prefix")
        exchange_code = match.group("exchange_code")
        phone_extension = match.group("phone_extension")
    else:
        raise ValueError("Invalid phone number.")


if __name__ == '__main__':
    for phone_number in ["+1 223-456-7890", "1-223-456-7890", "+1 223 456-7890", "(223)456-7890", "1 223456 7890", "223.456.7890."]:
        normalize(phone_number)
