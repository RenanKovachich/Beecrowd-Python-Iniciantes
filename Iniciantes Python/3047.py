m = int(input())
a = int(input())
b = int(input())
c = m - (a+b)

if a > b and a > c:
    print(a)

if b > a and b > c:
    print(b)

if c > b and c > a:
    print(c)