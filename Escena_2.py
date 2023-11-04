from cmu_graphics import*
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
segunda_escena()
cmu_graphics.run()