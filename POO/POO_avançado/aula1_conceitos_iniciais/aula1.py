class MinhaClasse:
    def __init__(self):  # Método construtor
        self.atributo_1 = [1, 2, "a"]

    def metodo_1(self, num):
        print("minha ação 1")
        print(self.atributo_1[1] + num)
        return "Olá mundo"

# Objeto

objeto1 = MinhaClasse()

resposta = objeto1.metodo_1(5)
print(resposta)

