while True:
    try:
        c, n = [int(x) for x in input().split()]
        msg = input()
        chave = input()
        A = msg.upper()
        B = chave.upper()
        a = msg.lower()
        b = chave.lower()
        for i in range(n):
            codigo = input()
            for j in codigo:
                if j in a:
                    print(b[a.find(j)], end="")
                elif j in b:
                    print(a[b.find(j)], end="")
                elif j in A:
                    print(B[A.find(j)], end="")
                elif j in B:
                    print(A[B.find(j)], end="")
                else:
                    print(j, end="")
            print()
        print()
    except EOFError:
        break

