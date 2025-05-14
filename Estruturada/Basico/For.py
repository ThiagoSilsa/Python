# for i in range(12,2,2):
#     print(i)

# # Para iterar cada caracter

# frase = "Lógica de programação e algoritimos"

# for i in range (0, len(frase), 1):
#     print(frase[i])

#     # O i vai de 0 até o valor máximo da string, e cada loop desse ele vai imprimir o caracter i da minha frase

# # Para imprimir tudo numa mesma linha:


# for i in range (0, len(frase), 1):
#     print(frase[i], end = "")


# Escrever algorítmo que calcule a média dos números pares de 1 até 100(1 e 100 inclusos). Imprementando o laço for

# soma = 0
# qtd = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         soma = soma + i
#         qtd = qtd + 1
# media = soma / qtd

# print(f"A média dos pares de 0 até 100 é :{media}")

# Algoritmo que calcule a tabuada de todos os números de 1 até 10 e para cad número a tabuada de 1 até 10

for i in range (1 , 11, 1):
    print(f'Tabuada do {i}')
    for a in range (1, 11 , 1):
        print(f'{i} X {a} = {i * a}')