def sub(x = 0 , y = 0):
    res = x - y
    print(res)
sub()

# Criar rotina que crie borda ao redor da palavra

def borda (s1):
    tam = len(s1)
    # Só irá escrever se tiver algo escrito
    if tam:
        print('+' , '-'*tam,'+')
        print('|', s1,'|')
        print('+' , '-'*tam,'+')

# Chamando programa
escrito = input('Qual a palavra?')
borda(escrito)


# Conceito de retornar dado ao escopo global:

# Procedimento != de função:

# Definiindo função com valores de 0 caso não seja atribuido nenhum valor
def soma (x = 0, y=0 , z= 0):
    res = x + y + z
    # Retornando valor de res
    return res
# Recebendo valor de res em "resultado"
resultado = soma(2,5,6)
print(resultado)


# Validador de tamanho de string

a = input('Escreva uma palavra')
b = int(input('Qual valor minimo?'))
c = int(input('Qual valor máximo?'))

def validador(texto, min, max):
    tam = len(texto)
    if (tam < max and tam > min):
        res = "Ta dentro"
    else:
        res = "Ta grande demais"
    return res

resultado = validador (a , b , c)
print(resultado)


## Função chamando a si mesma para resolver problema:


def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        fato = n * fatorial(n - 1)
        return fato
    
print(fatorial(5))

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
        

            
        