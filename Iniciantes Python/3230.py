w, p = map(int, input().split())

x1, y1, x2, y2 = [], [], [], []

paralelo = True
msm = 0

for i in range(p):
    xx1, yy1, xx2, yy2 = map(int, input().split())
    x1.append(xx1)
    y1.append(yy1)
    x2.append(xx2)
    y2.append(yy2)

    paralelo = paralelo and (x2[i] - x1[i]) * (y2[0] - y1[0]) - (y2[i] - y1[i]) * (x2[0] - x1[0]) == 0 or i == 0

    for j in range(i):
        if (x2[i] - x1[i]) * (y2[j] - y1[j]) - (y2[i] - y1[i]) * (x2[j] - x1[j]) == 0 and (x2[i] - x1[i]) * \
                (y2[i] - y1[j]) - (y2[i] - y1[i]) * (x2[i] - x1[j]) == 0:
            msm += 1
            break

p -= msm

if paralelo:
    if w <= p + 1:
        print(0)
    else:
        print(max(1, (w + 1) // 2 - p))
else:
    print(max(0, (w + 1) // 2 - p))
