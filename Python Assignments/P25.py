# Inputs

# 16  Input One
# 24  Input Two

# Needed Output

# "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
# "Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+

age = int(input("What's your age ? "))

if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")

else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

print("=" * 50)

# Inputs

# "Osama" First Name
# "Mohamed" Second Name

# Needed Output

# "Hello {First_Name} {First_Letter_From_Second_Name}." Example "Osama M."

first_name = input("Enter your first nam: ").strip().capitalize()
last_name = input("Enter your last nam: ").strip().capitalize()

print(f"Hollo {first_name} {last_name[:1]}")
