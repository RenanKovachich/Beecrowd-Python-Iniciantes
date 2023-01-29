while True:
    try:
        n = int(input())
        values = [int(x) for x in input().split()]
        pro = contra = 0
        for i in range(n):
            if values[i] == 1:
                pro += 1
            else:
                contra += 1

        if pro >= (n*2)/3:
            print('impeachment')
        else:
            print('acusacao arquivada')

    except EOFError:
        break
