def get_people_scores(name=None, **scores):
    if not scores:
        if name:
            print("Hello Ahmed You Have No Scores To Show")

    elif name and scores:
        print(f"Hello {name} This Is Your Score Table:")

    for subject, score in scores.items():
        print(f"{subject} => {score}")


# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"
print("-" * 40)

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
# "Hello Mahmoud This Is Your Score Table:"
# "Logic => 70"
# "Problems => 60"
print("-" * 40)

# Test 3
get_people_scores(Logic=70, Problems=60)

# Output
# "Logic => 70"
# "Problems => 60"
print("-" * 40)

# Test 4
get_people_scores("Ahmed")

# Output
# "Hello Ahmed You Have No Scores To Show"
