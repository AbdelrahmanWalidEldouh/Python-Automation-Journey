# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"

ignoredCount = 0
i = 0
while i < len(friends):
    if friends[i][0].islower():
        ignoredCount += 1
    else:
        print(friends[i])
    i += 1
print(f"Friends Printed And Ignored Names Count Is {ignoredCount}")

print("#" * 45)

# Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:

    print(skills.pop(0))

# Needed Output
# "HTML"
# "CSS"
# "JavaScript"
# "PHP"
# "Python"
