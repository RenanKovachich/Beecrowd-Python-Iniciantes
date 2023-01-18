casos = 1
while True:
    try:

        number_inputed = input()
        number_check = input()

        print('Caso #{}:'.format(casos))

        count = number_check.count(number_inputed)
        if count == 0:

            print('Nao existe subsequencia')

        else:

            print('Qtd.Subsequencias: {}'.format(count))
            count = number_check.rfind(number_inputed)
            print('Pos: {}'.format(int(count)+1))

        print()

        casos += 1

    except EOFError:
        break
