q = int(input())
for p in range(q):
    e = [int(x) for x in input().split()]
    print(len(str(e[0] ** e[1])))