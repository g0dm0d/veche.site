a = str(input())
b = str(input())
c = str(input())
z = 0
if a == b:
	z = z + 1
if a == c:
	z = z + 1
elif b == c:
	z = z + 1
if z == 1:
	print('Два числа одинаковые')
if z == 2:
	print('Все числа одинаковые')
if z == 0:
	print('Нет одинаковых чисел')