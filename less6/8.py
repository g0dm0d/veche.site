a = int(input())
b = []
while a != 0:
    b.append(a)
    if len(b) < 5:
        a = int(input())
    else:
        break
for i in b:
    print(i)
