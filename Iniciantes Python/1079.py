x = int(input())

for i in range(x):
    num_lidos = input()
    num_float = [float(m) for m in num_lidos.split()]
    p1 = num_float[0]
    p2 = num_float[1]
    p3 = num_float[2]

    conta = ((p1*2)+(p2*3)+(p3*5))/10

    print('{:.1f}'.format(conta))
