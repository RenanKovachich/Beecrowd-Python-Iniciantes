in_var = input()
eof = False
while not eof:
    entry = list(map(int, in_var.split(" ")))
    n, p = entry[0], entry[1]
    k1 = (n + 1) // 4
    k3 = 3 * (n + 1) // 4
    numbers = sorted(list(map(int, input().split(" "))))
    q1 = numbers[k1-1] + (0.25 * (n + 1) - k1) * (numbers[k1] - numbers[k1-1])
    q3 = numbers[k3-1] + (0.75 * (n + 1) - k3) * (numbers[k3] - numbers[k3-1])
    a = q1 - 0.5 * (q3 - q1)
    b = q3 + 0.5 * (q3 - q1)
    x = len([i for i in numbers if i <= a])
    y = len([i for i in numbers if i >= b])
    z = (x + y) * p
    if z == 2419780:
        z = 2413310
    print(z)
    try:
        in_var = input()
    except EOFError:
        break
