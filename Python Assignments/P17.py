# Needed Output

# "Osama"
# <class 'tuple'>

name = ("Osama",)
print(name[0])
print(type(name))

print("---------------------------")

nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements

nums_and_letters_one = nums + letters
print(f"nums_and_letters_one = {nums_and_letters_one}")
print(f"{ len( nums_and_letters_one ) } Elements")
