class MinhaClasse:
    def __init__(self) -> None:
        # Valor como privado, deve ser mantido como privado!
        self.__valor = None

    # Devo criar método especial para alterar o valor dentro da classe!
    # Esse método não retorna nada por isso o -> None!
    def setter(self, valor: int) -> None:
        self.__valor = valor

    # Para receber o valor deve-se implementar método getter!
    def getter(self) -> int:
        return self.__valor        

# Criando objeto:
my_class = MinhaClasse()

# Alterando valor de None para algum outro inteiro
my_class.setter(42)

# Recebendo o valor na va "valor"
valor = my_class.getter()
print(valor)
