from cmu_graphics import *
#klk
def quinta_escena():
    #Carretera
    Poligono(40, 400, 160, 0, 240, 0, 360, 400, relleno='grisTurbio')
    Linea(200, 0, 200, 400, relleno='blanco', anchuraDeLinea=6, guión= (12,14))
    #Anden
    Poligono(0, 0, 160, 0, 40, 400, 0, 400, relleno='grisOscuro')
    Poligono(240, 0, 400, 0, 400, 400, 360, 400, relleno='grisOscuro')
    #
    Poligono(240, 0, 250, 0, 375, 400, 360, 400, relleno=gradiente('oro', 'verde','oro','verde','oro','verde','oro','verde','oro','verde'))
    Poligono(150, 0, 160, 0, 40, 400, 25, 400, relleno=gradiente('oro', 'verde','oro','verde','oro','verde','oro','verde','oro','verde'))
    Linea(240, 0, 360, 400, anchuraDeLinea=1)
    Linea(160, 0, 40, 400, anchuraDeLinea=1)
    #
    #detalles
    Line(156,0,36,400,anchuraDeLinea=10,fill=gradient("oro","verde","oro","verde","oro","verde","oro","verde","oro","verde","oro","verde"))
    Line(244,0,364,400,anchuraDeLinea=10,fill=gradient("oro","verde","oro","verde","oro","verde","oro","verde","oro","verde","oro","verde"))
    Line(269,75,270,25,anchuraDeLinea=4)
    Line(270,25,260,25)
    Oval(263,29,8,7,fill="oro")
    Line(295,160,298,107,anchuraDeLinea=4)
    Line(298,107,288,107)
    Oval(291,110,8,7,fill="oro")
    Line(43,357,37,304,anchuraDeLinea=4)
    Line(37,304,47,304)
    Oval(45,308,8,7,fill="oro")
    Line(69,265,65,218,anchuraDeLinea=4)
    Line(65,218,75,218)
    Oval(73,222,8,7,fill="oro")

    #banca
    Line(67,172,70,184)
    Line(55,172,59,182)
    Line(76,186,55,182)
    Line(87,134,87,147)
    Line(77,129,74,145)
    Line(93,148,67,140)
    Rect(40,144,50,8,rotarÁngulo=-60,fill="naranjaMarrón")
    Rect(50,150,50,8,rotarÁngulo=-60,fill="naranjaMarrón")

    #arboles
    Line(48,236,34,201,anchuraDeLinea=10,fill="marrón")
    Circle(15,191,10,fill="green")
    Circle(26,196,10,fill="green")
    Circle(38,192,10,fill="green")
    Circle(28,180,10,fill="green")
    Circle(38,175,10,fill="green")
    Circle(25,165,10,fill="green")
    Circle(13,175,10,fill="green")

    Line(101,122,85,83,anchuraDeLinea=10,fill="marrón")
    Circle(73,79,10,fill="green")
    Circle(87,75,10,fill="green")
    Circle(84,64,10,fill="green")
    Circle(64,62,10,fill="green")
    Circle(62,73,10,fill="green")
    Circle(74,58,10,fill="green")
    Circle(73,65,10,fill="green")
    texto=Group(Rotulo("Que bonita quedó",200,200),
                Rotulo("la calle.Por fin",200,210),
                Rotulo("la arreglaron",200,220))
    texto.centroX=340
    texto.centroY=180
    burbuja=Group(
    Oval(texto.centroX,texto.centroY,110,60,fill=None,borde="negro"),
    Circle(326,218,6,fill=None,borde="negro"),
    Circle(333,228,4,fill=None,borde="negro"),

    )

    #Alcantarilla
    Poligono(115, 149, 128, 149, 122, 190, 103, 189, relleno='grisPizarraOscuro')
    Linea(126, 157, 112, 157)
    Linea(125, 166, 111, 166)
    Linea(124, 176, 108, 176)
    Linea(115, 149, 128, 149)
    Linea(128, 149, 122, 190)
    Linea(122, 190, 103, 189)
    señora=Group(
    Circulo(25, 154, 13),
    Linea(25, 154, 25, 214),
    Linea(24, 174, 36, 187),
    Linea(26, 174, 12, 187),
    Poligono(25, 194, 11, 214, 39, 214),
    Linea(20, 211, 20, 222),
    Linea(30, 211, 30, 222),
    Circulo(25, 140, 5)
    )

    #brillitos
    Estrella(100, 333, 3, 4, relleno='blanco')
    Estrella(254, 169, 3, 4, relleno='blanco')
    Estrella(175, 36, 3, 4, relleno='blanco') 
    señora.centroX=350
    señora.centroY=270

    Auto=Group(
    Ovalo(108,249,28,12,fill='white',rotarÁngulo=-20),
    Ovalo(167,249,40,15,fill='white',rotarÁngulo=20),
    Poligono(106,228,179,228,175,335,100,333,fill='white'),
    Rect(109,237,60,90),
    Rect(117,257,45,45, fill='white'),
    Line(162,257,169,237,fill='white'),
    Line(117,257,109,237,fill='white'),
    Line(162,302,169,327,fill='white'),
    Line(117,302,109,327,fill='white'),
    Ovalo(164,231,10,7,fill='amarillo'),
    Ovalo(112,231,10,7,fill='amarillo')
    )

    def enPaso():

        Auto.centroX=200
        Auto.centroY-=5
        
        if Auto.centroY<0:
            Auto.centroY =400
#quinta_escena()
#cmu_graphics.run()