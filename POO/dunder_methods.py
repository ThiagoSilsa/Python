# Principais dunder methods são:

# __init__(self)
# Construtor da classe, onde irá ser inserido as características do objeto

# __str__(self)
# Quando usar print no objeto irá retornar uma representação prédefinida do mesmo

# __len__(self)
# Usado para retornar o tamanho da lista quando uma lista é inserida numa classe e um objeto é criado a partir dai
# Resumindo, usado para informar o tamanho do objeto

# __add__(self)
# Para determinar o uso do operador + para objetos

# __eq__(self, other)
# Para comparação entre objetos

# __getitem__(self, index)
# Acessar elementos igual uma lista
# ________________________________________________________________________________________________________________________________________________________________


# __str__(self)
# Quando usar print no objeto irá retornar uma representação prédefinida do mesmo
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Pessoa:{self.nome}\nEmail:{self.email}"


# Criando objeto:
pessoa1 = Cliente("Thiago", "Thiago@gmail.com")
# print(pessoa1.nome)
# print(pessoa1)

# ________________________________________________________________________________________________________________________________________________________________


# __len__(self)
# Usado para retornar o tamanho da lista quando uma lista é inserida numa classe
# __getitem__(self, index)
# Acessar elementos igual uma lista
class Listagem:
    def __init__(self, dados):
        self.dados = dados

    def __len__(self):
        return len(self.dados)
    def __getitem__(self, index):
        return self.dados[index]


# A classe listagem receb a lista [1,2,3]
# Criando o objeto lista1
lista1 = Listagem([10, 20, 33])

print(len(lista1))
print(lista1[2])


# ________________________________________________________________________________________________________________________________________________________________

# __add__(self)
# Para determinar o uso do operador + para objetos

class Numero:
    def __init__(self, valor):
        self.valor = valor
        
    def __add__(self, outro):
        return self.valor + outro.valor
    
a = Numero(2)
b = Numero(5)

# print(a + b) 

# ________________________________________________________________________________________________________________________________________________________________
# __eq__(self, other)
# Para comparação entre objetos

class Nome():
    def __init__(self, nome):
        self.nome = nome
    def __eq__(self, value):
        return self.nome == value.nome 
        pass
    
u1 = Nome('Pedro')
u2 = Nome('Pedro')
u3 = Nome('João')

# print(u1 == u2)
# print(u1 == u3)