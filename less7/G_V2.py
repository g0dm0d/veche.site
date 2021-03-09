a = int(input())
data = []
answer = 0
while a > 0:
    if a % 10 == 4 or a % 10 == 6:
        answer += 1
    else:
        data.append(a % 10)
    a //= 10
for i in data:
    for z in data:
        if i + z == 6 or i + z == 4:
            answer += 1
answer /= 2
print(round(answer))