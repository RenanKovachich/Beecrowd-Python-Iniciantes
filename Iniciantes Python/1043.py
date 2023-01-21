a, b, c = [float(x) for x in input().split()]
if a < b+c and b < a+c and c < b+a:
    print('Perimetro = {:.1f}'.format(a+b+c))
else:
    print('Area = {:.1f}'.format((a+b)*c/2))
