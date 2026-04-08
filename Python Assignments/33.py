def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    print(f"Hello {name} Your Age Is {age} And You Live In {country}")


print(say_hello("Osama", 38, "Egypt"))

print(say_hello())

print("*" * 40)


def get_score(**scores):
    for subject, score in scores.items():
        print(f"{subject} => {score}")


get_score(Math=90, Science=80, Language=70)
print("-" * 30)
get_score(Logic=70, Problems=60)
