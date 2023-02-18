import sys


def coluna_para_indice(coluna):
    valor = 0
    for c in coluna:
        valor = valor * 26 + ord(c) - 64
        if valor > 16384:
            return None
    return valor


for linha in sys.stdin:
    coluna = linha.strip()
    indice = coluna_para_indice(coluna)
    if indice is not None:
        print(indice)
    else:
        print("Essa coluna nao existe Tobias!")
