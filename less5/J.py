v = int(input())
t = int(input())
s = v * t
if s > 0:
	while s > 108:
		s = s - 109
	print(s)
if s < 0:
	while abs(s) > 108:
		s = s + 109
	print(109 + s)