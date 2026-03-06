def calculate(number1, number2, action="add"):
    action = action.lower()
    if action == "add" or action == "a":
        return number1 + number2
    if action == "subtract" or action == "s":
        return number1 - number2
    if action == "multiply" or action == "m":
        return number1 * number2
    else:
        print("Invalid Operation !")


# Tests
print(calculate(10, 20))  # 30
print(calculate(10, 20, "AdD"))  # 30
print(calculate(10, 20, "a"))  # 30
print(calculate(10, 20, "A"))  # 30

print(calculate(10, 20, "S"))  # -10
print(calculate(10, 20, "subTRACT"))  # -10

print(calculate(10, 20, "Multiply"))  # 200
print(calculate(10, 20, "m"))  # 200
