# Princípio da responsabilidade única:

class SistemaCadastral:
    def cadastrar(self, nome : str, idade: int) -> None:
        if isinstance(nome,str) and isinstance(idade,int): #1
            print('Acessando banco de dados...') #2
            print(f'Cadastrar uduários {nome}, idade: {idade}') #3
        else:
            print('Dados inválidos!!')
            
# Várias responsabilidades no mesmo método!
pessoa1 = SistemaCadastral()