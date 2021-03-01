a = int(input())
if a < 10 ** 9:
    while a > 0:
        print(a%10,end = '\n')
        a //= 10