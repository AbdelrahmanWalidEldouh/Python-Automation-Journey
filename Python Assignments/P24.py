num_one = 10
num_two = 20

# Needed Output

# 30
# 27000
# 1000
# 200.0
# <class 'str'>

resulte = num_one + num_two
print(resulte)

print(resulte**3)

print(resulte**3 % 26000)

print((resulte**3 % 26000) / 5)

print(type(str((resulte**3 % 26000) / 5)))

print("=" * 30)

# Input
# "     osAmA   "

# Needed Output

# "Hello Osama, Happy To See You Here."

name = input("Enter your name: ").strip().capitalize()

print(f"Hello {name}, Happy To See You Here.")
