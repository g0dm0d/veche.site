a = int(input()[-1::-1])
z = 0
if a < 10 ** 9:
    while a > 0:
        x = a%10
        a //= 10
        z += x
print(z)
