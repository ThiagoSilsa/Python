class Interruptor:
    def __init__(self, comodo: str)-> None:
        self.comodo = comodo
        
    def acender(self)-> None:
        print(f'Acendendo a luz do cômodo {self.comodo}') 
        
    def apagar(self)-> None:
        print(f'Apagando a luz do cômodo {self.comodo}') 
        
        
class Pessoa():
    def acender_luzes(self, interruptor : Interruptor): # Necessário dizer o tipo pois assim é entendido de onde está vindo o interruptor. 
        interruptor.acender()
    
    def apagar_luzes(self, interruptor : Interruptor):
        interruptor.apagar()
        
    def dormir(self):
        print('Foi dormir!zzZZzzZZZzzZZzz')
        
        
agnaldo = Pessoa()
Interruptor_sala = Interruptor('sala')
Interruptor_quarto = Interruptor('quarto')

agnaldo.acender_luzes(Interruptor_sala)
agnaldo.apagar_luzes(Interruptor_quarto)