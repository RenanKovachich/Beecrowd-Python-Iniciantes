a = []
for i in range(int(input())):
    a.append(int(input()))
if max(a) == a[0]:
    print('S')
else:
    print('N')
    