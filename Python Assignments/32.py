def addition(*numbers):
    resulte = 0
    for i in numbers:
        if i == 10:
            continue
        elif i == 5:
            resulte -= i
        else:
            resulte += i

    return resulte


# Tests
print(addition(10, 20, 30, 10, 15))  # 65
print(addition(10, 20, 30, 10, 15, 5, 100))  # 160
