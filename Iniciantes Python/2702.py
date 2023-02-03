t = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]

total = 0
for i in range(3):
    j = w[i] - t[i]
    if j > 0:
        total += j

print(total)
