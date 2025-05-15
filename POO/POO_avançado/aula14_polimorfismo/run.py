# Polimorfismo

# Mesmo método pode ser utilizado de maneiras distintas

class ClasseQualquer():
    def fazer (self):
        print('Estou fazendo uma coisa!')

class ClasseQualquerCoisa(ClasseQualquer):
    def fazer (self):
        print('estou fazendo outra coisa!')


def fazer_func():
    print('Fazendo uma coisa a mais!')


obj1 = ClasseQualquer()
obj2 = ClasseQualquerCoisa()


obj1.fazer()

# Existe para esse objeto dois métodos fazer()
# Da classe mãe e de sua classe, ele irá executar o mais específico, da sua classe!
# Polimorfismo: Métodos iguais
obj2.fazer()

# Posso substituir a função fazer por uma função externa:
obj2.fazer = fazer_func

print(obj2.fazer())