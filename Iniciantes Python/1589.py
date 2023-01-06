number = int(input())
for i in range(number):
    x = input().split()
    R1, R2 = x

    R1, R2 = int(R1), int(R2)

    total = R1 + R2
    print(total)
    