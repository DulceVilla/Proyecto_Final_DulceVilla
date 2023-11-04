from cmu_graphics import *

#Escena1

from escena1 import primera_escena
from Escena_2 import segunda_escena
def enRatónPresionado(x,y):
        ambulancia.centroY -=5
        if ambulancia.centroY <50:
            ambulancia.centroY =50
            personas.visible=False
            persona3.visible=True
        
from escena_3 import tercera_escena
def colorAleatorio(valor):
        if valor == 1:
            return 'negro'
        
        if valor == 2:
            return 'rojo'
        
        if valor == 3:
            return 'azulGandul'

        if valor == 4:
            return 'verde'
def dibujarPersona(x, y):
        color = colorAleatorio(rangoAleatorio(1,5))
        Ovalo(x,y,25,50, relleno=color)
        Circulo(x,y-30,13, relleno=color)
        Linea(x-5,y+40,x-5,y, relleno=color)
        Linea(x+5,y+40,x+5,y, relleno=color)
        Rect(x-12,y+5,23,23, relleno=color)
        Ovalo(x+10,y-60,25,20,relleno='blanco')
        PoligonoRegular(x,y-53,7,3,rotarAngulo=-25,relleno='blanco')

def enRatónPresionado(x,y):
        brazo.centroY=263      
def enRatónSoltado(x,y):
        brazo.centroY=255
        if y >275:
            dibujarPersona(x, y)  
from escena_4 import cuarta_escena
def enTeclaPresionada(tecla):
        if tecla=="espacio":pala1.centroX+=2
        def enTeclaSoltada(tecla):
            if cemento.opacidad>=5:
                  cemento.opacidad-=5
        if tecla=="espacio":
            pala1.centroX-=2
            if carretilla.centroY <=200:
                persona2.centroX+=4
                persona2.centroY+=4
                carretilla.centroX+=4
                carretilla.centroY+=4
            while carretilla.centroY>199:
                carretilla.centroY=115
                carretilla.centroX=159
                persona2.centroX=148
                persona2.centroY=96
                cemento.opacidad+=100

from escena_5 import quinta_escena
def enPaso():

        Auto.centroX=200
        Auto.centroY-=5
        
        if Auto.centroY<0:
            Auto.centroY =400
primera_escena()
def enTeclaPresionada(tecla):
    print(tecla)
    if tecla =='a':
        segunda_escena()
        print("arriba")
    elif tecla == 'b':
        tercera_escena()
    elif tecla == 'c':
        cuarta_escena()
    elif tecla == 'd':
        quinta_escena()

cmu_graphics.run()