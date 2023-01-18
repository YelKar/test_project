import re

import requests

with requests.get("https://amperkot.ru/msk/contacts/") as res:
    text = res.text
exp = re.compile(r"\+7 ?\(?\d{3}\)? ?\d{3}-?\d{2}-?\d{2}")
print(re.findall(exp, text))
print(list(
    filter(lambda x: x, re.split(r"[()\- ]", "+7 (915) 194-50-18"))
))
