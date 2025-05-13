# Dataclasses facilitam pois os parâmetros já são definidos, logo, suas ações e metodos também

from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    email: str
    idade: int
    lista: list


lista1 = [20, 40, 60, 80, 100]
# Da forma abaixo: especificando posso inserir sem informar importar a ordem
# Pois está especificado onde cada dado irá
gui = Cliente(nome="Gui", email="Gui@gmail.com", lista=lista1, idade=15 )

# Nesse caso, devo respeitar a ordem, caso altere os dados irão ser armazenados em variáveis distintas
gui = Cliente("Gui","Gui@gmail.com", 15, lista1)

print(gui.nome)
print(gui.lista[1])
print(gui)
print(len(gui.lista))

# O que antes era necessário inserir método para printar o objeto com o __str__;
# Ou necessário __len__ para saber tamanho de algo;
# Ou __getitem__ para saber o ítem com id, agora é só usar o dataclasses
