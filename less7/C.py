a = int(input())
x = 0
for i in range(1, a+1):
	if i % 2 != 0:
		x += i
print(x)