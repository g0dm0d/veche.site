a = int(input())
for i in reversed(range(a - 1, 0, -1)):
    a *= i
print(a)
