def reverse_string(my_string):
    for index in range(len(my_string) - 1, -1, -1):
        yield my_string[index]


# Reverse The String
for c in reverse_string("Elzero"):
    print(c)
