friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


def get_names(name):
    return name[-1] == "m"


names = filter(get_names, friends_filter)

for i in names:
    print(i)

print("-" * 20)

for i in filter(lambda x: x[-1] == "m", friends_filter):
    print(i)
