from cmu_graphics import *

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
Circle(161,84,5)
Line(161,84,161,104)
Line(159,88,172,95)
Line(159,88,163,100)
Line(161,104,168,116)
Line(161,104,155,115)

#personitas
persona1=Group(
    Circulo(230,188,5),
    Line(230,188,230,213),
    Line(230,213,224,225),
    Line(230,213,236,225),
    Line(230,197,219,205),
    Line(230,197,241,205)
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
    
cmu_graphics.run()

    
    
    
    
    