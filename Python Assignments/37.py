# v = ??

# my_range + v = 820 ==> v = 820 - (0 + 1 + 2 + 3...+ 39) = 40

v = 40
my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

print("*" * 20)

# n = ??

# (0 + 1 + 2 + ...n-1) / n = 10 ==> 200 / 20 = 10 and range(20) = (0 + 1 + 2 ...39) = 200

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

    print("Good")

# Output => Good
