from cmu_graphics import *
##Carrretera##

Rect(0,0,400,400,relleno='grisoscuro')
Polygon(40,400,160,0,240,0,360,400,fill='gristurbio',borde='black')
Line(200,0,200,400,relleno='white',anchuraDeLinea=6,guión=(12,14))

##Daños##
Polygon(158,24,142,69,153,64,163,71,177,66,185,56,190,28,152,25,fill='white',borde='gris')
Polygon(263,88,277,138,259,132,244,141,244,121,213,116,217,97,239,98,263,88,fill='white',borde='gris')
Polygon(139,76,158,80,172,92,169,126,166,264,139,287,107,296,70,304,fill='azualaciano')
Polygon(311,249,307,270,267,284,232,264,245,240,284,228,fill='white',borde='gris')
Polygon(130,104,146,107,130,160,113,160,fill='gris',borde='black')
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
Ovalo(45,308,8,7,fill="oro")
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



cmu_graphics.run()