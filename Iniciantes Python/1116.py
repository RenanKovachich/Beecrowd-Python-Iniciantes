n = int(input())

for num in range(n):
    x = [float(x) for x in input().split()]
    num1 = float(x[0])
    num2 = float(x[1])

    if num1 == 0:
        print(0.0)
    elif num2 == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(num1/num2))
