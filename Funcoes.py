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