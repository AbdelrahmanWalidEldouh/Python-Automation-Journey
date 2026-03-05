word = "WWWooorrlld"


def cleanWord(w):
    if len(w) == 1:
        return w[0]

    if w[0] == w[1]:
        return cleanWord(w[1:])

    return w[0] + cleanWord(w[1:])


print(cleanWord(word))

print("=" * 30)


greating = lambda name, age: f"Hello {name} Your Age Is {age}"

print(greating("Abdelrahman", 19))
