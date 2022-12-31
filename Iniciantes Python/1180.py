numbers = int(input())

num_lidos = input()
num_list = [int(m) for m in num_lidos.split()]

ordenada = sorted(num_list)

print('Menor valor: {}'.format(ordenada[0]))

number_searched = num_list.index(ordenada[0])

print('Posicao: {}'.format(number_searched))

    
