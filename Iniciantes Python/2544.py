while True:
    try:
        n = int(input())
        p = 0
        while n > 1:
            n //= 2
            p += 1
        print(p)
    except EOFError:
        break
