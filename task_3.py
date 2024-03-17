import re

def normalize_phone(phone_number: str):
    number = "".join((re.findall(r'\d|\+', phone_number)))
    return f"+38{number[-10:]}"