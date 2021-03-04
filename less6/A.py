money = 5000
a = int(input())
while a > 0:
	money = round(money + 5000 * 0.04 / 12)
	a -= 1
print(money)
