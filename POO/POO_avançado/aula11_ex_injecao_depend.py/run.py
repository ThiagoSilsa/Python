
# Classe apenas de conexão!
class ConectorBancoDeDados:
    # Por padrão está sem conexão
    def __init__(self) -> None:
        self.connection = None
    # Conexão é estabelecida

    def conectar_ao_banco(self):
        self.connection = True


# Classe onde irá acontecer o CRUD!
class RepositorioDeBanco():
    def __init__(self, conexao: ConectorBancoDeDados):
        # Injeção de dependecia como privado
        self.__conexao = conexao

    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1, 2, 3, 4, 5]
        return None

# Ação que realizamos!


class RegraDeNegocio:
    # Precisamos buscar no repositório:
    def __init__(self, repo: RepositorioDeBanco):
        self.__repo = repo

    def calcular_resultados(self):
        # Recebendo a lista
        dados = self.__repo.busca_dados()
        if not dados:
            # Se não receber:
            print('Dados não encontrados, verifique conexão com o banco!')
        else:
            # Se receber:
            resposta = 0
            # Iterando a lista
            for dado in dados:
                resposta += dado
            print(f'O resultado e´ {resposta}')


# Conector de banco de dados!
conn = ConectorBancoDeDados()

# Estabelecendo conexão com o banco de dados -> True!
# Caso isso não ocorra, conexão irá falhar!
conn.conectar_ao_banco()

# Recebendo banco de dados, lista
repo = RepositorioDeBanco(conn)

# criando a regra
regra = RegraDeNegocio(repo)

regra.calcular_resultados()
