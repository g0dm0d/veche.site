z = int(input())
x = 0
for i in range(0,z,1):
    a = int(input())
    if a < 100 and a > x:
        x = a
print(x)