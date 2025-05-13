# Só o básico
# O main.py irá apenas chamar algumas funções do utilitário

# Importando as funções de utilitários, sendo que o utilitario está importando as classes de outros dois arquivos
from utilitarios import saldo_total, cadastrar_categoria, cadastrar_transacao

# Cadastrando categoria e recevendo-a em uma var
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas fixas")
categoria_viagens = cadastrar_categoria("Viagens")
categoria_lazer = cadastrar_categoria("Lazer")


# Cadastrando transaões, isso poderia ser feito com um menu interativo, mas como exemplo serviu
cadastrar_transacao(
    descricao="Salário Jan/2024", valor=100.0, categoria=categoria_receitas
)
t1 = cadastrar_transacao(
    descricao="Salário Jan/2024", valor=1000.0, categoria=categoria_receitas
)
t2 = cadastrar_transacao(
    descricao="Mesada Mamãe", valor=50.0, categoria=categoria_receitas
)
t3 = cadastrar_transacao(
    descricao="Ingresso Show", valor=-150.0, categoria=categoria_lazer
)
t4 = cadastrar_transacao(
    descricao="Conta de luz", valor=-100.0, categoria=categoria_contas
)
t1 = cadastrar_transacao(
    descricao= "Disney",
    valor= -400.0,
    categoria= categoria_viagens
)

# Saldo total
total = saldo_total()
print(f'Saldo total: {total}')

