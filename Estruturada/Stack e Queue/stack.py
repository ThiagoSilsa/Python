## LIFO
# Sistema de empilhamento


texto = []

while True:
    try:
        print('1 - Adicionar item\n2 - Remover item\n3 - Mostrar pilha')
        opt = int(input('>>'))
        if opt == 1:
            algo = input('Oque irá adicionar?')  
            texto.append(algo)
        elif opt == 2:
            print('Removendo último ítem')
            texto.pop()
        elif opt == 3:
            print(texto)
        else:
            print('Opção inválida!')
            
    except:
        print('Algo deu errado!')
        
