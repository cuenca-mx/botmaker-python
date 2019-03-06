import re

SANITIZE_PHONE_NUMBER = re.compile(r'[+.()\-\s]')


def sanitize_phone_number(phone_number):
    return SANITIZE_PHONE_NUMBER.sub(r'', phone_number)
