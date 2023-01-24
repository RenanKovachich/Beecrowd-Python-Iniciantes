a, b, c = [int(x) for x in input().split()]
if a < b+c and b < a+c and c < a+b:
    if a != b and b != c and a != c:
        print('Valido-Escaleno')
        if a**2 == b**2 + c**2 or c**2 == a**2 + b**2 or b**2 == a**2 + c**2:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif a == b and b == c and a == c:
        print('Valido-Equilatero')
        if a**2 == b**2 + c**2 or c**2 == a**2 + b**2 or b**2 == a**2 + c**2:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    else:
        print('Valido-Isoceles')
        if a**2 == b**2 + c**2 or c**2 == a**2 + b**2 or b**2 == a**2 + c**2:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
else:
    print('Invalido')