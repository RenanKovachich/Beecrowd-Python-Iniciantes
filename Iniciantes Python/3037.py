n = int(input())

while n > 0:
    m, j = 3, 3
    pts_1, pts_2 = 0, 0
    while j > 0:
        x, d = map(int, input().split())
        pts_1 += x * d
        j -= 1
    
    while m > 0:
        x, d = map(int, input().split())
        pts_2 += x * d
        m -= 1

    if pts_1 > pts_2:
        print('JOAO')
    else:
        print('MARIA')
    n -= 1