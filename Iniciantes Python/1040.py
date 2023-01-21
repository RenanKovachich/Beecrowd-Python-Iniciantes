n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10

if media >= 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
elif 5 <= media < 7:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    if (exame+media) / 2 >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format((exame+media)/2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format((exame + media) / 2))
