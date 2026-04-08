import random

print(f"Random Number Between 10 And 50 => {random.randint(10, 50)}")

print("-" * 40)

print(f"Random Even Number Between 2 And 10 => {random.randrange(2, 11, 2)}")

print("-" * 40)

print(f"Random Odd Number Between 1 And 9 => {random.randrange(1, 10, 2)}")

print("-" * 40)

print(dir(random))
