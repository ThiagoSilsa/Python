# Princípio de Liskov:
# Classe filha deve ser capaz de herdar as funcionalidades da classe mãe, sem excessões.

# Quebra do princpio de Liskov:


class Animal():
    def alimentar(self):
        print('O animal está se alimentando')

class Cachorro(Animal):
    def latir(self):
        print('O cachorro está latindo')

class Peixe(Animal):
    def nadar(self):
        print('O peixe está nadando')

    # Polimorfismo:
    def latir(self):
        # Exceção a regra do pai
        raise Exception ('Peixe não late!')
    
def verificar_animal(animal : any):
    animal.latir()


obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()

verificar_animal(obj3)