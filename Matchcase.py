print('Escolha uma opção')


while True:
    opt = int(input('1, 2 ou 3: '))
    match (opt):
        case 1:
            print('Você escolheo a opção 1')
        case 2:
            print('Você escolheo a opção 2')
        case 3:
            print('Você escolheo a opção 3')
        case 0:
            break
        case _ :
            print('Caso inexistente')