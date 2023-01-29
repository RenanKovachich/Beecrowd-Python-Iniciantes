while True:
    try:
        n, a_min, a_max = [int(x) for x in input().split()]
        casos = 0
        for i in range(n):
            a = int(input())
            if a_max >= a >= a_min:
                casos += 1

        print(casos)
    except EOFError:
        break
