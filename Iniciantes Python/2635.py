v = list()
t = 0
for g in range(int(input())):
    v.append(str(input()))
for g in range(int(input())):
    msg = input()
    q = 0
    for i in v:
        if i.startswith(msg):
            q += 1
            t = len(i)
            if q != 1:
                if len(i) > t:
                    t = len(i)
                else:
                    t = len(i) + len(msg)
    if q != 0:
        print(q, t)
    else:
        print(-1)
