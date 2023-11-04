from cmu_graphics import*
def tercera_escena():
    Rect(0,0,400,400,relleno='bronceado')
    Rect(11,190,230,85,relleno='gris')
    Poligono(11,11,11,190,241,190,389,147,389,11,relleno='gris')
    Poligono(241,190,389,147,390,338,375,337,375,313,357,308,355,270,314,269,306,292,293,293,
        291,265,258,264,252,274,241,275,relleno='gris')
    Linea(11,190,241,190)
    Linea(241,190,389,147)
    Linea(238,190,236,275)
    Rect(33,206,185,66,relleno='azulclaro',borde='negro')


    numero = 0


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

    #director
    Circulo(178,231,13,relleno='madera')
    Ovalo(177,268,25,50,relleno='azulcielo')
    Linea(170,297,170,310,relleno='madera')
    Linea(182,297,182,310,relleno='madera')
    Rect(165,276,23,23,relleno='azul')
    brazo=Poligono(168,255,144,252,168,265,relleno='madera')
    Poligono(187,265,205,283,188,273,relleno='madera')
    Ovalo(143,216,30,25,relleno='blanco')
    PoligonoRegular(150,224,10,3,relleno='blanco')
        
        
def enRatónPresionado(x,y):
        brazo.centroY=263

        
def enRatónSoltado(x,y):
        brazo.centroY=255
        if y >275:
            dibujarPersona(x, y)   
#tercera_escena()
#cmu_graphics.run()