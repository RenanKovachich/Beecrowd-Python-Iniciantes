e = input()
a = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
q = 0
for i in a:
    if not i in l:
        q += 1
print(q)
