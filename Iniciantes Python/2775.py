while True:
    try:
        n = int(input())
        if n == 0:
            break
        p = [int(x) for x in input().split()]
        v = [int(x) for x in input().split()]
        m = list(zip(p, v))
        m.sort()
        soma = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if m[i][0] > m[j][0]:
                    soma += m[i][1] + m[j][1]
                    m[i], m[j] = m[j], m[i]
        print(soma)
    except EOFError:
        break
