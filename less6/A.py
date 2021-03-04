money = 5000
month = int(input())
for i in range (month):
	money = money + (money * 0.04 / 12)
print(round(money))