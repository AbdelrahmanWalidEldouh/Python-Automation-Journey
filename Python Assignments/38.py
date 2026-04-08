friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]


def remove_chars(name):
    return name[1:-1]


cleaned_list = map(remove_chars, friends_map)

for i in cleaned_list:
    print(i)

print("-" * 20)

for i in map(lambda x: x[1:-1], friends_map):
    print(i)
