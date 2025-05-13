# Posso chamar um método dentro de outro método

class Clientes:
    def __init__(self, nome):
        self.nome = nome
    def exibir(self):
        print(f'O nome é {self.nome}')
    def chamar_exibir(self):
        self.exibir()
        
        
pessoa1 = Clientes('Guilherme')

pessoa1.chamar_exibir()