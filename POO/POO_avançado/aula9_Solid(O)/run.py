# Aberto a extensão e fechado a modificação!


# Está ferindo o princípio de modificação pois cada nova apresentação será necessário alterrar todo o 
# Código fonte


class Circo:
    def apresentar(self, command:int) ->None:
        if command == 1:
            self.__show_palhaço()
        elif command == 2:
            self.__show_malabarista()
        elif command == 3:
            self.__show_magico()
            
    def __show_palhaço():
        print('O palhaço está se apresentando!')
    def __show_malabarista():
        print('O malabarista está se apresentando!')
    def __show_magico():
        print('O mágico está se apresentando!')
        
        
circo = Circo()

command = 3

circo.apresentar(command)