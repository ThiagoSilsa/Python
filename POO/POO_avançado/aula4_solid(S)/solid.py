# Princípio da responsabilidade única:

class SistemaCadastral:
    def cadastrar(self, nome : str, idade: int) -> None:
        if self.__validate_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__tratamento_de_erros()
            
    # Função de validação separada
    def __validate_input(self, nome: str, idade: int):
        return isinstance(nome,str) and isinstance(idade,int)
    
    # Função de registro separada
    def __register_user(self, nome:str, idade:int) ->bool:
        print('Acessando banco de dados...') 
        print(f'Cadastrar uduários {nome}, idade: {idade}')
            
    # Tratamento de erros
    def __tratamento_de_erros(self):
        print('Dados inválidos')
        
pessoa1 = SistemaCadastral()
pessoa1.cadastrar(5, 25)

