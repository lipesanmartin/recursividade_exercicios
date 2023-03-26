#  4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

def somar_lista(tamanho: int) -> int:
    if tamanho <= 1:
        return lis[0]
    return lis[n - 1] + somar_lista(n - 1)


if __name__ == '__main__':
    lis = []
    while True:
        novo_numero = int(input("Insira um inteiro para adicionar à lista. (0 ou negativo termina): "))
        if novo_numero <= 0:
            break
        else:
            lis.append(novo_numero)
    n = len(lis)
    if n == 0:
        print("Lista vazia")
    else:
        print(somar_lista(n))