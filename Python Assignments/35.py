scores_list = {"Math": 90, "Science": 80, "Language": 70}


def get_the_scores(name=None, **scores):
    if scores and not name:
        for subject, score in scores.items():
            print(f"{subject} => {score}")

    if name and not scores:
        print(f"Hello {name} You Have No Scores To Show")

    if scores and name:
        print(f"Hello {name} This Is Your Score Table:")
        for subject, score in scores.items():
            print(f"{subject} => {score}")


# Test 1
get_the_scores("Osama", **scores_list)

# Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"
print("-" * 30)

# Test 2
get_the_scores("Osama")

# Output
# "Hello Osama You Have No Scores To Show"
print("-" * 30)

# Test 3
get_the_scores(**scores_list)

# Output
# "Math => 90"
# "Science => 80"
# "Language => 70"
