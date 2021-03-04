R = int(input())
A = int(input())
Pi = float(3.14)
R = R ** 2 * Pi
A = A ** 2
if R == A:
	print('равны')
elif R > A:
	print('круг')
else:
	print('квадрат')
