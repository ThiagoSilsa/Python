# Usando o conhecimento de classes para Clientes de uma plataforma de streaming


# Dont matter if class have () or not
class Clientes():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        
        # Só posso ter dois planos possíveis, logo não preciso que o cliente me informe isso
        self.lista_planos = ['BASIC','PREMIUM']
        # Se o plano escolhido é válido:
        if plano.upper() in self.lista_planos:
            self.plano = plano.upper()
        else:
            print('Plano inválido')

    def mudar_plano(self, novo_plano):
        # Variáveis com self se comunicam entre funções, pois são características do objeto.
        # A variável self.lista_planos estava na def init, mas é acessável auqi também.
        if novo_plano.upper() in self.lista_planos:
            self.plano = novo_plano.upper()
        else:
            print('Plano inválido!')
    
    def ver_filmme(self, filme, plano_filme):
        if self.plano.upper() == plano_filme or self.plano.upper() == "PREMIUM":
            print(f'Ver filmes {filme}')
        elif self.plano.upper() == "BASIC" and plano_filme == "PREMIUM":
            print('Faça upgrade para PREMIUM para ver o filme')
        else:
            print('Plano inválido')

# Criei o objeto cliente1
cliente1 = Clientes('Thiago', "Thiago@gmail.com", "basic")

# Acesso qualquer característica desse cliente
print(f'O plano antigo é: {cliente1.plano}')
cliente1.ver_filmme("Harry Potter", "PREMIUM")
# Posso mudar alguma característica também
# mudando o plano:

cliente1.mudar_plano('premium')

print(f'O novo plano é: {cliente1.plano}')
cliente1.ver_filmme("Harry Potter", "PREMIUM")

