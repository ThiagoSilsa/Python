


# Fila do banco
# FIFO
from collections import deque

fila = deque()

while True:
    try:
        print('1 - Adicionar pessoa na fila\n2 - Atender pessoa\n3 - Mostrar fila')
        opt = int(input('>>'))
        if opt == 1:
            algo = input('Qual nome da pessoa?')  
            fila.append(algo)
        elif opt == 2:
            print(f'Atendendo primeira pessoa {fila[0]}')
            fila.popleft()
        elif opt == 3:
            print(fila)
        else:
            print('Opção inválida!')
            
    except:
        print('Algo deu errado!')
        