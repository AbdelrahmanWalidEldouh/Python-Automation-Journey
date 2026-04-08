skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

counter = 50
for skill in reversed(skills):
    if type(skill) == str:
        print(f"{counter} - {skill}")
        counter += 1

print("-" * 20)


skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

index = 50

reversed_skills = skills[::-1]

for skill in reversed_skills:
    if skill != 10 and skill != 20:
        print(f"{index} - {skill}")
        index += 1
