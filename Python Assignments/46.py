import re

phone_re = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

mo = phone_re.search("My number is 555-123-1234")

print(mo.group(1))

print(mo.group(2))

print(mo.group(0))

print(mo.group())
