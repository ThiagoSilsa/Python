class Pessoa:
    def __init__(self, nome, altura, idade):
        self.nome = nome
        self.altura = altura
        self.idade = idade

    def correr(self):
        print("Estou correndo")

    def comer(self):
        print("Estou comendo")


# Criando o objeto

pessoa1 = Pessoa("Thiago", 1.75, 24)

print(f'O {pessoa1.nome} tem {pessoa1.altura} cm de altura e {pessoa1.idade} anos')
pessoa1.comer()
pessoa1.correr()
