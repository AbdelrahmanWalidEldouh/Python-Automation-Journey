friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print('"' + friends[0] + '"' + " => Method One")
print(f'"{ friends[0] }" => Method two')

print('"' + friends[-1] + '"' + " => Method One")
print(f'"{friends[-1]}" => Method two')


print("------------------------")

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"

print(friends[::2])
print(friends[1::2])

print("-----------------------------------")

friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.insert(0, "Nasser")
print(friends)

friends.append("Salem")
print(friends)
