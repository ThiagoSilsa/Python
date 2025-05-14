# Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de livros. Este software deve ter o seguinte menu e opções:


# 1)	Cadastrar Livro
# 2)	Consultar Livro
    # 1.	Consultar Todos 
    # 2.	Consultar por Id
    # 3.	Consultar por Autor
    # 4.	Retornar ao menu
# 3)	Remover Livro
# 4)	Encerrar Programa

print('Bem-vindo a livraria do Thiago Santos')
print('-'*40)



lista_livro = []
id_global = 0


def cadastrar_livro(id):
    '''
        Armazena nome, autor, editora e id em um dicionário chamado "item"
        Depois, adiciona o item à lista "lista_livro"
    '''
    print('-'*40)
    print('-'*9+' Menu Cadastrar livro ' + '-'*9)
    print(f'Id do livro : {id}')
    nome = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o nome do autor do livro')
    editora = input('Por favor entre com a editora do livro')
    item = {
        "id" : id,
        "nome" : nome,
        "autor" : autor,
        "editora" : editora
        }
    lista_livro.append(item)
   
def consultar_livro():
    print('-' * 40)
    print('-'*9+' Menu consultar livro ' + '-'*9)
    while True:
        try:
            opcao = int(input('Escolha entre a opção desejada: \n1 - Consultar todos os livros\n2 - Consultar livro por id\n3 - Consultar livro(s) por autor\n4 - Retornar ao menu principal'))
            match opcao:
                case 1:
                    for livro in lista_livro:
                        
                        # Está devolvendo o valor (value) da chave (key), "id", "nome", etc...
                        
                        print(f'Id: {livro["id"]}')
                        print(f'Nome: {livro["nome"]}')
                        print(f'Autor: {livro["autor"]}')
                        print(f'Editora: {livro["editora"]}')
                case 2:
                    id_escolhido = int(input('Digite o id do livro'))
                    
                    # Será realizada a iteração dos livros na lista_livros
                    # Caso a chave "id" do livro seja igual ao id desejado "id_escolhido"
                    # Irá printar os dados do livro em questão.
                    
                    for livro in lista_livro:
                        if livro["id"] == id_escolhido:
                            print(f'Id: {livro["id"]}')
                            print(f'Nome: {livro["nome"]}')
                            print(f'Autor: {livro["autor"]}')
                            print(f'Editora: {livro["editora"]}')
                case 3:
                    autor_escolhido = input('Digite o nome do autor do(s) livros: ')
                    
                    # Mesma iteração do caso anterior, dessa vez utilizando o autor
                    # Foi utilizado a função upper() para não ter problema ao escrever minúsculo ou maíusculo o nomedo autor.
                    
                    for livro in lista_livro:
                        if livro["autor"].upper() == autor_escolhido.upper():
                            print(f'Id: {livro["id"]}')
                            print(f'Nome: {livro["nome"]}')
                            print(f'Autor: {livro["autor"]}')
                            print(f'Editora: {livro["editora"]}') 
                case 4 :
                    
                    # Quebra o laço while dessa função e volta ao laço principal do menu principal
                    
                    print('Retornando ao menu principal')
                    break
                case _:
                    print('Opção inválida')
        except:
            print('Opção inválida, tente novamente')

def remover_livro():
        try:
            id_remover = int(input("Qual id do livro a ser removido?"))
            
            # Foi utilizado o "enumerate" pois assim é possível consultar o valor do índice de cada livro para poder
            # Removê-lo com o del lista_livro[indice]
            
            for indice, livro in enumerate(lista_livro):
                if livro["id"] == id_remover:
                    del lista_livro[indice]
                    print('livro removido com sucesso!')
                    
                    # Caso remova o livro irá printar e o return irá rodar, encerrando o for e função
                    
                    return
            print('Livro com esse ID não foi encontrado')
        except:
            print('Erro entrada inválida')
    
    
# MENU PRINCIPAL
while True:
    print('-'*12+' Menu principal ' + '-'*12)
    print('Escolha a opção desejada:\n1 - Cadastrar livro\n2 - Consultar livro(s)\n3 - Remover livro\n4 - Sair')
    try:
        opt = int(input('>>'))
        if opt == 1:
            
            # Somando id global para sempre adicionar livro com id maior que o anterior
            id_global = id_global + 1 
            
            # Chamando função de cadastrar livro
            
            cadastrar_livro(id_global)
        elif opt == 2:
            
            # chamando função de consultar livro
            consultar_livro()
            
        elif opt == 3:
            
            # Chamando função de remover livro
            
            remover_livro()
        elif opt == 4:
            print('Finalizando programa...')
            break
        else:
            print('Opção inválida!')
    except:
        print('Algo deu errado!')
        
        