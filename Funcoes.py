def imprime(nome):
    print('Esta é uma função. Meu nome é ' + nome)


imprime("Amós")


def potencia(n):
    return n * n


print(potencia(3))


def intervalo(inic=1, fim=10):
    for inic in range(inic, fim+1):
        print(inic)


# Funções com valores default não exigem argumentos ao chama-la
intervalo()