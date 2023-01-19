while True:
    t = int(input())
    if t == 0:
        break
    else:
        for i in range(t):
            n = int(input())
            if n % 2 == 0:
                print(2*n-2)
            else:
                print(2*n-1)
