#  Determing tuple

# bag = ("axe", "coat", "bacon", "avocado")

# for i in range (0 , len(bag), 1):
#     print(f'Na minha  tem {bag[i]}')
# ---------------------------------------------------------
# Upgrade

# bag = ("axe", "coat", "bacon", "avocado")
# upgrade = ("banana", "knife")

# big_bag = bag + upgrade
# print(big_bag)


# #
# def soma(*num):
#     acumulador = 0
#     print(f"Tupla: {num}")
#     for i in num: #Número não precisa saber o tamanho, ele irá iterar
#         acumulador += i
#     return acumulador

# print(f'O resultado: {soma(1,2,3,4,5,6,7,8,9)} \n')

# Listas:
# lista1 = [1,2,3,4,5]
# lista2 = lista1[:]

# lista2[0]=10
# print(lista1)

# String dentro de listas:

# mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']

# for item in mochila:
#     for letra in item:
#         print(letra)
#     print()
    
# for i in range(0, len(mochila),1):
#     for j in range (0, len(mochila[i]),1):
#         print(mochila[i][j], end= '')
#     print()

# Lista de mercado

# item = []
# mercado = []

# for i in range (0,3,1):
#     item.append(input('Digite o nome do item: '))
#     item.append(int(input('Digite a quantidade do item: ')))
#     item.append(float(input('Digite o preço do item: '))) # coloquei três itens dentro do item
#     mercado.append(item[:]) # coloco os três itens como um só item em mercado
#     item.clear() #limpo a lista e começo novamnente
# print(mercado)

# soma = 0
# print('Lista de compras')
# print('-' * 20)
# print('item | Quantidade | Valor unitário | Total do item')
# for item in mercado:
#     print(f'{item[0]} | {item[1]} | {item[2]} | {item[1]*item[2]}')
#     soma = soma + (item[1]*item[2])
# print('-' * 20)
# print(f'O total é {soma} reais')

