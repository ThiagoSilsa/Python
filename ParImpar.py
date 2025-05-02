# Par e Ímpar


def parimpar(x):
    '''
        Função retorna:
        1 = Par
        2 = Ímpar
        3 = Erro de formatação, inteiro ou string errados
    '''
    try:
        if int(x) % 2 == 0 :
            res = 1
        else:
            res = 2
    except:
        res = 3
    return res
    
    
while True:
    num = input('Qual o número a ser testado?')
    if num == "0":
        break
    else:
        res = parimpar(num)
        match res:
            case 1:
                print(f'O número {num} é par')
            case 2:
                print(f'O número {num} é ímpar')
            case 3:
                print('Algo deu errado tente novamente!')
        

            
        