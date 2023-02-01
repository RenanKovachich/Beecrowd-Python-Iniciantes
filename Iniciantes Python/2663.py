n = int(input())
k = int(input())
pont = []
count = k
for i in range(n):
    number = int(input())
    pont.append(number)

pont = sorted(pont, reverse=True)

while count < n and pont[count] == pont[k-1]:
    count += 1

print(count)
