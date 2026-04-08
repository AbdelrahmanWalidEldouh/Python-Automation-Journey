from functools import reduce


nums = [2, 4, 6, 2]


def multiply(number1, number2):
    return number1 * number2


resulte = reduce(multiply, nums)

print(resulte)
