# Encapsulamento
# Publico
# _Protegido
# __Privado

class Mamifero():
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao

    def andar(self):
        print(f'O mamífero esta´ andando pelo {self.localizacao}')

    def _dormir(self):
        print('O animal está dormindo')

        
class Gato(Mamifero):
    def __init__(self, localizacao, nome):
        super().__init__(localizacao)
        self.nome = nome

    def miar(self):
        self.andar()
        print(f'O {self.nome} está miando!')
        self._dormir()


gato = Gato('Brazil', 'Bernardo')

gato.miar()

gato.andar()
gato._dormir()