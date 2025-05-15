# Injeção de dependencias !!


# Celular tem seus atributos e suas funções
class Celular:
    def __init__(self, modelo: str):
        self.modelo = modelo

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f"Enviando mensagem: \n{mensagem}")

    def abrir_emails(self) -> None:
        print("Abrindo os E-mails!")

    def abrir_youtube(self) -> None:
        print("Abrindo o Youtube!")


# Crio os celular
android = Celular("Samsung")
iphone = Celular("Iphone")

# Pessoa tem a ação mas depende de celular para ser criada
# Pessoa também depende do celular para executar as ações.


# Em outras palavras "Pessoa utiliza as funcionalidades do celular"
class Pessoa:
    # Pessoa só pode ser criada se tiver um celular
    def __init__(self, celular: Celular, nome: str):

        self.celular = celular
        self.nome = nome

    # Utilizando as funções do celular
    def pedir_pizza(self):
        self.celular.enviar_mensagem("Calabresa Gigante!")
        print(f"Enviado por celular modelo: {self.celular.modelo}")

    def estudar(self):
        print(f"{self.nome} está sentando para estudar...")
        self.celular.abrir_youtube()


# Criando objeto pessoas dependendo do objeto celular
marilene = Pessoa(iphone, "Marilene")
thiago = Pessoa(android, "Thiago")


thiago.pedir_pizza()
thiago.estudar()

# Aqui é estranho pois seria como o celular da marilene tivesse abrindo os emails sozinho.
marilene.celular.abrir_emails()
