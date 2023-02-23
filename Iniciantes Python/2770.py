import sys

while True:
    try:
        inputs = list(map(int, sys.stdin.readline().split()))
        x, y, m = inputs[0], inputs[1], inputs[2]
        min_dim, max_dim = min(x, y), max(x, y)

        for i in range(m):
            inputs = list(map(int, sys.stdin.readline().split()))
            xi, yi = inputs[0], inputs[1]
            if xi <= min_dim and yi <= max_dim:
                print('Sim')
            elif xi <= max_dim and yi <= min_dim:
                print('Sim')
            else:
                print('Nao')
    except:
        break
