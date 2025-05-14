
# i= 0 
# while True:
#     try:
#         nome = input('Por favor digite seu nome: ')
#         ind = int(input('Digite índice'))
#         print(nome[ind])
#         break
#     except ValueError:
#         print('Nome inválido, tente novamentee')
#     except IndexError:
#         print('índice inválido, tente novamente')
#     finally:
#         print(f'tentativa {i}')
#         i += 1

# def div():
#     try:
#         num1 = int(input('número 1'))
#         num2 = int(input('número 2'))
#         res = num1/num2
#     except ZeroDivisionError:
#         print('Divisão pro zero!')
#     except:
#         print('Algo de errado aconteceu')
#     else: # Se não tiver excessão roda o else
#         return res
#     finally:
#         print('Sempre irá ocorrer')

# # programa principal
# print(div())

        
# Função lambda:

# soma = lambda x : x+x

# print(soma(2))