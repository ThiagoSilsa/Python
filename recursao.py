## Função chamando a si mesma para resolver problema:


def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        fato = n * fatorial(n - 1)
        return fato
    
print(fatorial(5))