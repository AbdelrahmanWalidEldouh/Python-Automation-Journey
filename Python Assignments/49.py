import re

pattern = re.compile(r"Java(Script)|Python")
search = pattern.search("I am learning JavaScript")

print(search.group())
