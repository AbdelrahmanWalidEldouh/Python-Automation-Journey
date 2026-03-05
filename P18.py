my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4

unique_list = [1, 2, 3, 4, 5]

print(unique_list)
print(type(unique_list))
print(unique_list[:4])

print("*************************")

nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

print(nums.union(letters))
print(nums | letters)
nums.update(letters)
print(nums)
