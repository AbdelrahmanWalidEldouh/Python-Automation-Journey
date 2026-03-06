# "Osama@Nn.Sa"  Email

# Needed Output

# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"

email = input("Pleas enter your email: ").strip().lower()

userName = email.capitalize()[: email.index("@")]
provider = email[email.index("@") + 1 : email.index(".")]
domain = email[email.index(".") + 1 :]

print(
    f"Your Name Is {userName} \nEmail Service Provider Is {provider} \nTop Level Domain Is {domain}"
)

print("@" * 30)

# Inputs

numX = input("Number One: ").strip()
num1 = int(numX)

numY = input("Number Two: ").strip()
num2 = int(numY)

operation = input("Operation: ").strip()

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

if operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "+":
    print(num1 + num2)
elif operation == "%":
    print(num1 % num2)
else:
    print("Wrong Operation!")
