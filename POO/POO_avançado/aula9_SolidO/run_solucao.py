class Artista():
    def __init__(self, tipo : str):
        self.tipo = tipo
        
    def apresentar_show(self) -> None:
        print(f'O {self.tipo} está apresentando seu show!')


class Circo:
    def apresentar(self, artista : Artista) ->None:
        artista.apresentar_show()
            
        
# Dessa forma gerenaliza-se o código.
# As únicas coisas que serão adicionadas serão mais objetos;
# "Palhaço, malabarista, apresentador, motoboy,..."
# É possivel fazer isso ficar melhor em forma dee inputs, armazeram objetos em listas e poder acessa-los...
# Pelo menos é oq eu imagino

circo = Circo()
palhaco = Artista('Palhaço')
magico = Artista('Mágico')

circo.apresentar(palhaco)
circo.apresentar(magico)