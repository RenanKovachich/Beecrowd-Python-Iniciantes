x, y, z = input().split()
x = float(x)
y = float(y)
z = float(z)

if x >= y and x >= z:
    a = x
    b = y
    c = z
if (y >= x) and (y >= z):
    a = y
    b = x
    c = z
if (z >= x) and (z >= y):
    a = z
    b = x
    c = y
if a >= (b + c):
    print('NAO FORMA TRIANGULO')
elif a * a == (b * b + c * c):
    print('TRIANGULO RETANGULO')
elif a * a > (b * b + c * c):
    print('TRIANGULO OBTUSANGULO')
elif a * a < (b * b + c * c):
    print('TRIANGULO ACUTANGULO')
if a == b and b == c:
    print('TRIANGULO EQUILATERO')
elif a == b or b == c:
    print('TRIANGULO ISOSCELES')
