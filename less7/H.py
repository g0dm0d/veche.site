answer = str('Yes')
for i in range(0,4,1):
    a = int(input())
    if a % 10 == 4:
        answer = str('No')
print(answer)