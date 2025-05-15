# Heranças

class Mamifero():
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao

    def andar(self):
        print(f'O mamífero esta´ andando pelo {self.localizacao}')


# O cachorro é um mamífero e como a "MAIORIA" dos mamíferos pode andar:
class Cachoro(Mamifero):
    # A função init irá receber a herança do Mamifero()
    def __init__(self, localizacao, nome):
        # Super() está referenciando o init da mãe
        super().__init__(localizacao)
        self.nome = nome

    def latir(self):
        # Posso acessar métodos da classe mãe
        self.andar()
        print(f'O {self.nome} está latindo!')


class Gato(Mamifero):
    def __init__(self, localizacao, nome):
        super().__init__(localizacao)
        self.nome = nome

    def miar(self):
        self.andar()
        print(f'O {self.nome} está miando!')


# Instanciando os animais, Todo animal tem uma localização por isso a localização está na mãe
# Já latir ou miar depende do tipo de animal, cachorro ou gato!
# "Todos" eles podem andar!
petruquio = Cachoro('Maricá', "Petruquio")
biscoito = Gato('Vilatur', "Biscoito")

petruquio.latir()
biscoito.miar()
