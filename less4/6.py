yearborn = int(input())
monthborn = int(input())
year = int(input())
month = int(input())
old = 0
if month < monthborn:
	old = year - yearborn - 1
else:
	old = year - yearborn
print(old)