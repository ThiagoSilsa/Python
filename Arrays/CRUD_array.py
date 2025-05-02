# Criar um programa que permita:

# Cadastrar as notas de vários alunos.

# Calcular a média das notas.

# Exibir as notas acima da média.

# Exibir a maior e menor nota.

# Permitir adicionar mais notas posteriormente.

import array as ar
notas = ar.array('f',[])

def add_nota():
    while True:
        try:
            nota = float(input('Qual nota a ser adicionada?'))
            notas.append(nota)
            break
        except:
            print('Algo deu errado!')

def cal_media():
    soma = 0
    qtd = 0
    for i in notas:
        soma = soma + i
        qtd += 1
        
    media = soma/qtd
    print(f'Média: {media:.2f}')
    return media

def acima_media():
    media = cal_media()
    for i in notas:
        if i >= media:
            print(f'{i} está acima da média!')
        
def maior_menor():
    print(f'Maior nota: {max(notas)}')     
    print(f'Menor nota: {min(notas)}')     
    

# Menu principal
while True:
    try:
        print('-'*10 + 'Menu principal' + '-'*10)
        print('Escolha uma opção:\n1 - Cadastrar nova nota\n2 - Calcular média das notas\n3 - Exibir notas acima da média\n4 - Exibir maior e menor nota\n5 - Sair')
        opt = int(input('>>'))
        if opt == 1:
            # Chamar função de add nota
            add_nota()
            print(f'Notas cadastradas: {[f"{n:.1f}" for n in notas]}')
        elif opt == 2:
            # Chamar função de calcular média das notas
            cal_media()
            print('Média calculada com sucesso!')
        elif opt == 3:
            acima_media()
            # Chamar função de calcular Exibir notas acima da média das notas
            print('Notas acima da média exibidas')
        elif opt == 4:
            # Chamar função de calcular Exibir maior e menor nota
            maior_menor()
            print('Maior e menor notas')
        elif opt == 5:
            print('Finalizando o programa')
            break
        else:
            print('Opção inválida!')
    except:
        print('Opção não aceita!')