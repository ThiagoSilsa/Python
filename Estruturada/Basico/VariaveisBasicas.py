
# Cálculo de preço de desconto:
prec = int(input('Qual valor do produto em reais?'))
desc = float(input('Qual porcentagem do desconto?'))


print(f'O valor do seu desconto de {desc}% em cima de R${prec} é de R${(desc/100)*prec} e preço final do produto é de R${prec*((100-desc)/100)}')

# Cálculo de gastos por aluguel de carro:

km = float(input('Quantos km foram percorridos ao total?'))
dia = int(input('Quantos dias de aluguel?'))


y = 60*dia + 0.15*km

print(f'O total a paga é R${y}')

# Criar variável de string que receba uma frase. Uma segunda variável irá receber metade da string digitada.
# Na tela será exibido os dois últimos caracteres da segunda variável tipo str

var1 = input('Digite uma frase qualquer')

# Tenho que forçar ser inteiro:
tam = int(len(var1)/2)

var2 = var1[0:tam]
print(f"A frase '{var1}' pela metada é '{var2}'")

tam2 = len(var2)
var3 = var2[(tam2-2):tam2]
print(f'O dois últimos digitos da segunda variável são:{var3}')
