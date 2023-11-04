import time 
from cmu_graphics import *
##Carrretera##
#escena1
def primera_escena():
    Rect(0,0,400,400,relleno='grisoscuro')
    Polygon(40,400,160,0,240,0,360,400,fill='gristurbio',borde='black')
    Line(200,0,200,400,relleno='white',anchuraDeLinea=6,guión=(12,14))

    ##Daños##
    Polygon(158,24,142,69,153,64,163,71,177,66,185,56,190,28,152,25,fill='white',borde='gris')
    Polygon(263,88,277,138,259,132,244,141,244,121,213,116,217,97,239,98,263,88,fill='white',borde='gris')
    Polygon(139,76,158,80,172,92,169,126,166,264,139,287,107,296,70,304,fill='azualaciano')
    Poligono(311,249,307,270,267,284,232,264,245,240,284,228,fill='white',borde='gris')
    Poligono(130,104,146,107,130,160,113,160,fill='gris',borde='black')
    Line(135,105,118,160)
    Line(139,107,124,159)

    ##Faro1##
    Line(156,0,36,400,anchuraDeLinea=10,fill=gradient('oro','verde','oro','verde','oro','verde','oro','verde','oro','verde','oro','verde'))
    Line(244,0,364,400,anchuraDeLinea=10,fill=gradient('oro','verde','oro','verde','oro','verde','oro','verde','oro','verde','oro','verde'))
    Line(269,75,270,25,anchuraDeLinea=4)
    Line(270,25,260,25)
    Oval(263,29,8,7,fill='oro',borde='black')

    ##Faro2##
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
#escena2
def segunda_escena():
    app.fondo="grisOscuro"

    #carretera
    Polygon(40,402,160,-2,240,-2,360,402,fill="grisTurbio",borde="negro"),
    LineaDeSeparacion=Line(200,0,200,400,fill="white",anchuraDeLinea=6,guion = (12,14))
    #daños
    Polygon(158,24,142,69,153,64,163,71,177,66,185,56,190,28,152,25,fill='white',borde='gris')
    Polygon(263,88,277,138,259,132,244,141,244,121,213,116,217,97,239,98,263,88,fill='white',borde='gris')
    Poligono(311,249,307,270,267,284,232,264,245,240,284,228,fill='white',borde='gris')
    Poligono(130,104,146,107,130,160,113,160,fill='gris',borde='black')
    Line(135,105,118,160)
    Line(139,107,124,159)

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
    banca=Group(Line(67,172,70,184),
    Line(55,172,59,182),
    Line(76,186,55,182),
    Line(87,134,87,147),
    Line(77,129,74,145),
    Line(93,148,67,140),
    Rect(40,144,50,8,rotarÁngulo=-60,fill="naranjaMarrón"),
    Rect(50,150,50,8,rotarÁngulo=-60,fill="naranjaMarrón")
    )

    #arboles
    arbol1=Group(Line(48,236,34,201,anchuraDeLinea=10,fill="marrón"),
    Circle(15,191,10,fill="green"),
    Circle(26,196,10,fill="green"),
    Circle(38,192,10,fill="green"),
    Circle(28,180,10,fill="green"),
    Circle(38,175,10,fill="green"),
    Circle(25,165,10,fill="green"),
    Circle(13,175,10,fill="green")
    )

    arbol2=Group(Line(101,122,85,83,anchuraDeLinea=10,fill="marrón"),
    Circle(73,79,10,fill="green"),
    Circle(87,75,10,fill="green"),
    Circle(84,64,10,fill="green"),
    Circle(64,62,10,fill="green"),
    Circle(62,73,10,fill="green"),
    Circle(74,58,10,fill="green"),
    Circle(73,65,10,fill="green")
    )


    #Arboles
    Linea(48,236,34,201,anchuraDeLinea=10,fill='marrón')
    Circulo(15,191,10,fill='green')
    Circulo(26,196,10,fill='green')
    Circulo(38,192,10,fill='green')
    Circulo(28,180,10,fill='green')
    Circulo(38,175,10,fill='green')
    Circulo(25,165,10,fill='green')
    Circulo(13,175,10,fill='green')

    Linea(101,122,85,83,anchuraDeLinea=10,fill='marrón')
    Circulo(73,79,10,fill='green')
    Circulo(87,75,10,fill='green')
    Circulo(84,64,10,fill='green')
    Circulo(64,62,10,fill='green')
    Circulo(62,73,10,fill='green')
    Circulo(74,58,10,fill='green')
    Circulo(73,65,10,fill='green')

    #Banca
    Linea(67,172,70,184)
    Linea(55,172,59,182)
    Linea(76,186,55,182)
    Linea(87,134,87,147)
    Linea(77,129,74,145)
    Linea(93,148,67,140)
    Rect(40,144,50,8,rotarÁngulo=-60,fill='naranjaMarrón')
    Rect(50,150,50,8,rotarÁngulo=-60,fill='naranjaMarrón')
    #persona
    personas = Grupo (
    Circulo(78,247,10),
    Ovalo(98,248,30,20,rotarAngulo=+15),
    Linea(111,247,121,249),
    Linea(108,256,117,257),
    Ovalo(30,270,180,40,fill='white',rotarAngulo=-100),
    Rotulo('Estas vias producen ',25,270,rotarAngulo=-100),
    Rotulo('muchos accidentes...',37,270,rotarAngulo=-100),

    #persona2
    Circulo(56,270,10),
    Ovalo(73,274,30,20,rotarAngulo=+20),
    Linea(81,280,93,280),
    Linea(85,270,92,270),
    Ovalo(110,205,150,40,relleno='blanco',rotarAngulo=-20),
    Rotulo('¡Jumm no hacen nada',110,200,rotarAngulo=-20),
    Rotulo('por arreglarlas!',110,210,rotarAngulo=-20),
    )
    #personas
    persona3 = Grupo(
    Circulo(106,34,10),
    Ovalo(117,47,30,20,rotarAngulo=+50),
    Linea(120,57,129,63),
    Linea(128,53,133,58),
    Circulo(128,18,10),
    Ovalo(140,31,25,20,rotarAngulo=+50),
    Linea(142,38,148,45),
    Linea(152,35,154,41),
    )

    persona3.visible=Falso 

    #ambulancia 
    ambulancia = Group(
    Circulo(254,199,5),
    Circulo(252,169,5),
    Circulo(216,169,5),
    Circulo(215,199,5),
    Rect(216,162,37,47,relleno='blanco'),
    Rect(228,147,14,19,relleno='blanco'),
    Linea(241,207,241,162,relleno='rojo'),
    Linea(227,208,227,163,relleno='rojo'),
    )

    def enRatónPresionado(x,y):
        ambulancia.centroY -=5
        if ambulancia.centroY <50:
            ambulancia.centroY =50
            personas.visible=False
            persona3.visible=True
    #Agua
    Circulo(172,55,30,relleno='azulClaro')

    #carro
    Circulo(188,33,3)
    Circulo(189,46,3)
    Circulo(163,33,3)
    Circulo(163,46,3)
    Rect(172,24,7,7,relleno='naranja')
    Rect(164,31,24,20,relleno='naranja')

#escena3
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

#escena4
def cuarta_escena():
    app.fondo="grisOscuro"

    #carretera
    Polygon(40,402,160,-2,240,-2,360,402,fill="grisTurbio",borde="negro")
    LineaDeSeparacion=Line(200,0,200,400,fill="white",anchuraDeLinea=6,guion = (12,14))

    primeraBalla=Group(
    Rect(90,343,6,20,fill="white"),
    Rect(107,343,6,20,fill="white"),
    Rect(84,363,35,6,fill="white"),
    Rect(80,320,45,10,fill="white"),
    Line(90,320,85,330,fill="red"),
    Line(100,320,95,330,fill="red"),
    Line(110,320,105,330,fill="red"),
    Line(120,320,115,330,fill="red"),
    Rect(80,333,45,10,fill="white"),
    Line(90,333,85,343,fill="red"),
    Line(100,333,95,343,fill="red"),
    Line(110,333,105,343,fill="red"),
    Line(120,333,115,343,fill="red"),
    )
    seguntaBalla=Group(
    Rect(289,343,6,20,fill="white"),
    Rect(308,343,6,20,fill="white"),
    Rect(284,363,35,6,fill="white"),

    Rect(280,320,45,10,fill="white"),
    Line(290,320,285,330,fill="red"),
    Line(300,320,295,330,fill="red"),
    Line(310,320,305,330,fill="red"),
    Line(320,320,315,330,fill="red"),

    Rect(280,333,45,10,fill="white"),
    Line(290,333,285,343,fill="red"),
    Line(300,333,295,343,fill="red"),
    Line(310,333,305,343,fill="red"),
    Line(320,333,315,343,fill="red"),
    )
    conosDeTransito=Group(
    RegularPolygon(164,75,15,3,fill=gradient("rojoNaranja","blanco","rojoNaranja",inicio="superior")),
    RegularPolygon(230,75,15,3,fill=gradient("rojoNaranja","blanco","rojoNaranja",inicio="superior"))
    )
    #daños
    Polygon(272,119,255,124,264,132,255,136,269,154,255,152,280,149,fill="grisTurbio")
    Polygon(272,119,255,124,264,132,255,136,269,154,255,152,280,149,fill=gradiente("gris","gris","grisOscuro","grisOscuro",inicio="derecha"),opacidad=80,borde="grisTurbio")
    Polygon(120,132,143,141,133,156,140,164,127,163,111,169,fill=gradiente("gris","grisTurbio","grisOscuro","grisOscuro",inicio="izquierda"))
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

    carretilla=Group(
    Circle(182,135,5,fill=None,borde="negro"),
    Polygon(168,112,185,108,191,124,187,132,fill="plateado",borde="negro"),
    Polygon(168,112,165,116,182,136,187,132),
    Line(170,112,163,100,fill="marrón"),
    Linea(180,110,172,95,fill="marrón")
    )
    persona2=Group(
    Circle(161,84,5),
    Line(161,84,161,104),
    Line(159,88,172,95),
    Line(159,88,163,100),
    Line(161,104,168,116),
    Line(161,104,155,115)
    )
    #personitas
    persona1=Group(
        Circulo(230,188,5),
        Line(230,188,230,213),
        Line(230,213,224,225),
        Line(230,213,236,225),
        Line(230,197,219,205),
        Line(230,197,241,205),
    )
        
            
    maquina=Group(
    Oval(130,227,24,29,rotarÁngulo=-26,fill=gradiente("grisClaro","amarillo","oro",inicio="izquierda"),borde="negro"),
    Polygon(121,236,140,218,147,233,134,245,fill=gradiente("grisClaro","amarillo","oro",inicio="izquierda"),borde="negro"),
    Oval(123,221,15,10,rotarÁngulo=-50,fill="grisTurbio",borde="negro"),
    Rect(100,243,50,10,fill="red",borde="negro"),
    Polygon(150,253,150,220,170,220,176,230,187,230,187,253,fill="red",borde="negro"),
    Polygon(154,225,165,225,172,236,154,236,fill="grisTurbio",borde="negro"),
    Circle(173,255,8,fill="grisTurbio",borde="negro"),
    Circle(115,256,8,fill="grisTurbio",borde="negro"),
    Line(150,243,142,235))

    cemento=Group(
    Oval(268,231,30,40,fill="plateado"),
    Rect(246,229,40,25,fill="grisTurbio"),
    )
    #palas
    pala1=Group(Linea(241,205,253,220,fill="marrón"),
        RegularPolygon(253,220,7,3,rotarÁngulo=+15,fill="gris",borde="negro",anchuraDeBorde=1))
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

#escena5
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
introducción=Rotulo('Para pasar a las escenas presione teclas',200,200,tamaño=20)
Rotulo('Inicia con la a',200,250,tamaño=20)

#trancisiones 
def enTeclaPresionada(tecla):
    print(tecla)
    if tecla=='a':
        primera_escena()
        Rotulo("presione b para la siguiente escena",200,320,tamaño=15,negrito=True)

    elif tecla =='b':
        segunda_escena()

        Rotulo("presione c para la siguiente escena",200,320,tamaño=15,negrito=True)
    elif tecla == 'c':
        tercera_escena()
        Rotulo("presione d para la siguiente escena",200,320,tamaño=15,negrito=True)
    elif tecla == 'd':
        cuarta_escena()
        Rotulo("presione e para la siguiente escena",200,310,tamaño=15,negrito=True)
    elif tecla == 'e':
        quinta_escena()


cmu_graphics.run()