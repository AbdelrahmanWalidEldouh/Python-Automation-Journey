my_friends = []
max_friends = 4

while len(my_friends) < max_friends:
    name = input("Enter Friend Name: ").strip()

    if name.isupper():
        print("Invalid Name")

    else:
        if name.islower():
            name = name.capitalize()
            print(f"Friend {name.lower()} Added => 1st Letter Become Capital")

        else:
            print(f"Friend {name} Added")

        my_friends.append(name)

        left_names = max_friends - len(my_friends)
        if left_names > 0:
            print(f"Names Left in List Is {left_names}")
        else:
            print("List Is Full")

print("*" * 50)

# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]

# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"

my_nums.sort(reverse=True)

count = 0

for num in my_nums:
    if num % 5 == 0:
        count += 1
        print(f"{count} => {num}")

print("All Numbers Printed")
