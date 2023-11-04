from cmu_graphics import *

#Escena1

from escena1 import primera_escena
from Escena_2 import segunda_escena
from escena_3 import tercera_escena
from escena_4 import cuarta_escena
from escena_5 import quinta_escena
primera_escena()
def enTeclaPresionada(tecla):
    print(tecla)
    if tecla == '2':
        segunda_escena()
        print("arriba")
    elif tecla =='3':
        tercera_escena()
    elif tecla =='4':
        cuarta_escena()
    elif tecla =='5':
        quinta_escena()

cmu_graphics.run()