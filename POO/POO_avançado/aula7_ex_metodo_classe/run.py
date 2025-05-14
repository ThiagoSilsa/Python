# Classe que é uma loja

class Loja():
    taxa = 1.15
    
    def __init__(self, valor : float, nome : str) -> None:
        self.valor_produto_bruto = valor
        self.nome = nome
        
    def consultar_valor_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f'A loja {self.nome} tem produto custando {valor_produto}')
        
    def consultar_taxa(self):
        return self.taxa
        
    @classmethod
    def editar_taxa_produto(cls, valor: float):
        cls.taxa = valor
        
        
# Menu
loja_praia = Loja(10.50, nome="Praia")
loja_shopping = Loja(23.50, nome="Shopping" )
loja_mercado = Loja(15.50, nome="Mercado")


while True:
    try:
        opt = int(input('1 - Consultar valor dos produtos\n2 - consultar taxas\n3 - Editar taxa de produto\n4 - Sair'))
        if opt == 1:
            loja_praia.consultar_valor_produto()
            loja_shopping.consultar_valor_produto()
            loja_mercado.consultar_valor_produto()
        elif opt == 2:
            print(f'A taxa atual é: {Loja.taxa}')
        elif opt == 3:
            valor = int(input('Qual o novo valor de taxa?'))
            loja_mercado.editar_taxa_produto(valor)
        elif opt == 4:
            break
        else:
            print('Opção inválida')
    except:
        ('Algo deu errado!')
        