while True:
    try:
        N, q = [int(x) for x in input().split()]
        m = []
        while N:
            N -= 1
            m.append(int(input()))
        m.sort(reverse=True)
        while q:
            q -= 1
            p = input()
            print(m[int(p) - 1])
    except EOFError:
        break
