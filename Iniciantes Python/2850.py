while True:
    try:
        e = input()
        if e == 'esquerda':
            print('ingles')
        elif e == 'direita':
            print('frances')
        elif e == 'nenhuma':
            print('portugues')
        else:
            print('caiu')
    except EOFError:
        break