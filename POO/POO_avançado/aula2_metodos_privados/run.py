class Pessoa():
    def __init__(self, altura, cpf):
        self.altura = altura
        self.__cpf = cpf
        
    def apresentar(self):
        print(f'Olá minha altura é {self.altura}')
        self.__coletar_documento()
        
    def __coletar_documento(self):
        print(f'Meu documento CPF é: {self.__cpf}')
        
        
joao_grilo = Pessoa(1.75, "154.652.657-05")
joao_grilo.apresentar()
