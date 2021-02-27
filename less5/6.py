a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
	print(min(b,c), max(b,c), a)
elif b >= a and b >= c:
	print(min(a,c), max(a,c), b)
elif c >= b and c >= a:
	print(min(b,a), max(b,a), c)