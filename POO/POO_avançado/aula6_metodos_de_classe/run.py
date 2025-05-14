
class MinhaClasse:
    estatico = "Banana"
    
    def __init__(self, estado: bool)-> None:
        self.__estado = estado        

    def print_var_classe(self):
        print(self.estatico)
        
    @classmethod
    def alter_var_classe(cls):
        cls.estatico = "AlgumaCoisa"

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.print_var_classe()
obj2.print_var_classe()
# Alterei toda a classe!!
obj2.alter_var_classe()

# Verificando novamente!
obj2.print_var_classe()
obj1.print_var_classe()


