age = 17

# Needed Output

# "App Is Suitable For You" # If Age Larger Than 16
# "App Is Not Suitable For You" # if Age Smaller Than 16

print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")


print("*" * 30)

# Input Example 38

# Needed Output
# "Your Age In Months Is 456 Months"   Months Example
# "Your Age In Weeks Is 1824 Weeks"   Weeks Example

ageX = input("Plea Write Your Age (In Years): ").strip()
age = int(ageX)

if age > 10 and age < 100:
    ageInMonths = age * 12
    ageInWeeks = ageInMonths * 4
    ageInDays = ageInWeeks * 7
    ageInHours = ageInDays * 24
    ageInMinutes = ageInHours * 60
    ageInSeconds = ageInMinutes * 60

    print(
        f"Your Age In Month Is {ageInMonths} Months\nYour Age In Weeks Is {ageInWeeks} Weeks\n"
        f"Your Age In Days {ageInDays} Days\nYour Age In Hours {ageInHours} Hours\n"
        f"Your Age In Minutes Is {ageInMinutes} Minutes\nYour Age In Seconds Is {ageInSeconds} Seconds"
    )

else:
    print("Invalid Input.")
