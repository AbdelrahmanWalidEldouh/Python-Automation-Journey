# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country: ").strip()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

# Needed Output
# "Your Country Eligible For Discount And The Price After Discount Is $70"  Egypt Example
# "Your Country Not Eligible For Discount And The Price Is $100"  Ghana Example

print(
    "Your Country Eligible For Discount And The Price After Discount Is $70"
    if country in countries
    else "Your Country Not Eligible For Discount And The Price Is $100"
)

print("*" * 40)

# Input
numX = input("Enter number less greater than 0: ")
num = int(numX)
forMsg = num - 2
if num > 0:
    while True:
        num -= 1
        if num == 6:
            continue
        if num == 0:
            break
        print(num)
else:
    print(f"Number {num} Is Not Larger Than 0")

print(f"{forMsg} Numbers Printed Successfully.")

# Needed Output
# 9
# 8
# 7
# 5
# 4
# 3
# 2
# 1
# "8 Numbers Printed Successfully."
