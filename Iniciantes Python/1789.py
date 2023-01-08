while True:
    try:
        number = int(input())
        values = input().split()
        m = 0
        for i in range(number):
            if int(values[i]) > m:
                m = int(values[i])

        if m < 10:
            N = 1
        elif 10 <= m < 20:
            N = 2
        else:
            N = 3
        print(N)

    except EOFError:
        break
