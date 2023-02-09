while True:
    try:
        x, y, m = map(int, input().split())
        for i in range(m):
            xi, yi = map(int, input().split())
            print('Sim' if (xi <= x and yi <= y) or (xi <= y and yi <= x) else 'Nao')
    except EOFError:
        break
