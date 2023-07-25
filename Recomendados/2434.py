def menor_saldo_conta(n, s, movimentacoes):
    menor_saldo = s
    saldo_atual = s

    for movimentacao in movimentacoes:
        saldo_atual += movimentacao
        if saldo_atual < menor_saldo:
            menor_saldo = saldo_atual

    return menor_saldo


n, s = map(int, input().split())
movimentacoes = [int(input()) for _ in range(n)]

resultado = menor_saldo_conta(n, s, movimentacoes)
print(resultado)
