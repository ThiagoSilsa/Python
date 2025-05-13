# Primeiro cria classe

class ControleRemoto:
    # O self é o proprio objeto
    # Função __ini__() é uma função interna do python que inicia a classe para criar o objeto
    def __init__(self, cor, altura, profundidade, largura):
        # Aqui é inserido as características do objeto
        # Caracteristicas (Algo fixo)
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    # Métodos: (Sempre verbos)
    def passar_canal(self, botao):
        if botao == "+":
            print('Aumentar canal')
        elif botao == "-":
            print('Dimunuir o canal')
        return
# Criando o controle remoto:
# controle_remoto1 usou a classe ControleRemoto() para ser criado (instancia)
controle_remoto1 = ControleRemoto("Preto","10cm","2cm","2cm")

# Posso mostrar uma única característica de um objeto
print(controle_remoto1.cor)

controle_remoto2 = ControleRemoto("Vermelho","10cm","2cm","2cm")
print(controle_remoto2.cor)


# Posso chamar a função como um método, assim como o upper()
# A função criada virou um método para o controle_remoto1
# Claro que antes foi preciso criar o controle remoto.
controle_remoto1.passar_canal("+")

# Logo, criei o código uma só vez, e posso usar diversas vezes de diversas formas
