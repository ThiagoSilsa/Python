# Caso a var estática da clase seja mudada irá mudar para todos os objetos também!!


class MinhaClasse:
    estatico = "Banana"


# É possível acessar a var dentro da classe
print(MinhaClasse.estatico)

# Criando objetos
obj1 = MinhaClasse()
obj2 = MinhaClasse()

# Printando var estática
print(obj1.estatico)
print(obj2.estatico)

# Alterando var estática
MinhaClasse.estatico = "programador"

# Printando var estática novamente
print(obj1.estatico)
print(obj2.estatico)

# Alterando apenas o estático do objeto 1

obj1.estatico = "Olá mundo!"
print(obj1.estatico)
