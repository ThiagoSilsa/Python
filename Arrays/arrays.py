# Primeiro deve-se importar o módulo array

# Módulo é um conjunto de funções, variáveis e classes

import array as ar

# Criando array de inteiros:

# A variável array_inteiros está recebendo o módulo "ar" que recebe a função de criar array
# O i indica que é um array de números inteiros
array_inteiros = ar.array('i',[1, 2, 3, 4, 5])

print(array_inteiros)

# Posso adicionar e remover elementos igual listas, usando o append e remove

array_inteiros.append(6)
print(array_inteiros)

array_inteiros.remove(3)
print(array_inteiros)

# Posso acessa seus índices como listas:
print(array_inteiros[2])
# E saber seu tamanho
print(len(array_inteiros))
array1 = ar.array('i',[1,5,2,5,4])

print(type(array1))