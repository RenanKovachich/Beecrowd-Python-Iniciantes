while True:
    try:
        alfabeto = input()
        frase = ''
        n = int(input())
        number = [int(x) for x in input().split()]
        for y in range(0, n):
            frase += alfabeto[number[y]-1]
        print(frase)
    except EOFError:
        break
