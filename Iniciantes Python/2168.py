quadras = int(input())
cameras = [input().split() for x in range(quadras+1)]

for x in range(quadras):
    for j in range(quadras):
        if int(cameras[x][j]) + int(cameras[x][j + 1]) + int(cameras[x + 1][j]) + int(cameras[x + 1][j + 1]) < 2:
            print('U', end='')
        else:
            print('S', end='')
    print()
