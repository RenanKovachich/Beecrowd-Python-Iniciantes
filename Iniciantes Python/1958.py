f = input()
if f[0] == '-':
    f = float(f)
    print(format(f, '.4E'))
else:
    f = float(f)
    f1 = format(f, '.4E')
    print('+{}'.format(f1))
