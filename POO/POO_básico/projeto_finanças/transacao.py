from dataclasses import dataclass

# Importando de outro arquivo python
from categoria import Categoria


@dataclass
class Transacao:
    descricao: str
    valor: float
    categoria: Categoria
    
    def exibir(self):
        # Deve-se usar o self.categoria.nome pois a Categoria é um objeto
        print(f'DESCRIÇÃO: {self.descricao} | VALOR: {self.valor} | CATEGORIA: {self.categoria.nome}')
    
