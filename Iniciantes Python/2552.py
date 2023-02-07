while True:
    try:
        N, M = map(int, input().split())
    except EOFError:
        break
    mat = []
    for i in range(N):
        mat.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                print("9", end="")
            else:
                p = 0
                if i > 0 and mat[i - 1][j] == 1:
                    p += 1
                if i < N - 1 and mat[i + 1][j] == 1:
                    p += 1
                if j > 0 and mat[i][j - 1] == 1:
                    p += 1
                if j < M - 1 and mat[i][j + 1] == 1:
                    p += 1
                print(p, end="")
        print("")
