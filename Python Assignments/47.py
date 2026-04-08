import re

phon_re = re.compile("(\d\d\d)-(\d\d\d\d\d\d\d\d)")

mo = phon_re.search(r"My phone number is 012-12345678")

n1, n2 = mo.groups()

print(n1, n2)
