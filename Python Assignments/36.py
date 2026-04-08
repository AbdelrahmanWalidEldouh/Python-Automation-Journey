# Define a tuple containing three integers: 0, 1, and 2
values = (0, 1, 2)

# The any() function returns True if at least one element in the iterable is True.
# Since 1 and 2 are non-zero (True in Python), this condition is met.
if any(values):
    # This block executes, initializing my_var with the value 0
    my_var = 0

# Create a list with various data types: Boolean, Integers, a List, a Float, and our variable
# my_list effectively becomes: [True, 1, 1, ["A", "B"], 10.5, 0]
my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# The all() function returns True only if EVERY element in the selection is True.
# Let's break down the OR conditions:
# 1. all(my_list[:4]) -> Checks [True, 1, 1, ["A", "B"]]. All are non-zero/non-empty, so it's True.
# 2. all(my_list[:6]) -> Checks the first 6 elements. The last one is 0 (False), so this is False.
# 3. all(my_list[:])  -> Checks the whole list. Since it contains 0, this is also False.
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    # Since the first part of the OR is True, Python uses "Short-circuit evaluation" and prints this.
    print("Good")
else:
    # This block is skipped because the IF condition was satisfied
    print("Bad")

# Predicted Output:
# Good
