from cmu_graphics import *

app.fondo="negro"
sol = Estrella(200,200,35,400,relleno=gradiente("naranja","amarillo","rojoNaranja"))

tierra = Grupo(
    Circulo(200,200,130,relleno=None,borde="grisOscuro"),
    Circulo(200,70,10,relleno=gradiente("verde","azulReal",inicio="izquierda-superior")),
    Circle(220,50,7,relleno="grisTurbio")
    )
    
mercurio = Grupo(
    Circulo(200,200,70,relleno=None,borde="grisOscuro"),
    Circulo(200,130,10,relleno="grisOscuro")
    )
    
venus = Grupo(
    Circulo(200,200,100,relleno=None,borde="grisOscuro"),
    Circulo(200,100,10,relleno="naranjaMarrón"))
    
marte = Grupo(
       Circulo(200,200,170,relleno=None,borde="grisOscuro",visible=False),
       Circulo(200,30,10,relleno="rojo"))
       

estrella = Estrella(320,40,5,5,relleno="blanco")
estrella1 = Estrella(200,40,5,5,relleno="blanco")
estrella2 = Estrella(320,160,5,5,relleno="blanco")
fugaz = Linea(320,40,350,20,relleno="blanco")
fugaz1 = Linea(200,40,230,20,relleno="blanco")
fugaz2 = Linea(320,160,350,140,relleno="blanco")

estrella1.dx=-10
estrella2.dx=-10
estrella.dx=-10
estrella.dy=+10
estrella1.dy=+10
estrella2.dy=+10
fugaz.dx=-10
fugaz1.dx=-10
fugaz2.dx=-10
fugaz.dy=10
fugaz1.dy=10
fugaz2.dy=10



tierra.direccion="sentido-horario"
mercurio.direccion="sentido-horario"
venus.direccion="sentido-horario"
marte.direccion="sentido-horario"

def enTeclaPresionada(tecla):
    
    
    if(tecla=="derecha"):
        tierra.direccion="sentido-horario"
        mercurio.direccion="sentido-horario"
        venus.direccion="sentido-horario"
        marte.direccion="sentido-horario"
    elif(tecla=="izquierda"):
        tierra.direccion="sentido-antihorario"
        mercurio.direccion="sentido-antihorario"
        venus.direccion="sentido-antihorario"
        marte.direccion="sentido-antihorario"
        
def enPaso():
    fugaz.x2=estrella.centroX+20
    fugaz1.x2=estrella1.centroX+20
    fugaz2.x2=estrella2.centroX+20
    fugaz.x1=estrella.centroX
    fugaz1.x1=estrella1.centroX
    fugaz2.x1=estrella2.centroX
    fugaz.y1=estrella.centroY
    fugaz1.y1=estrella1.centroY
    fugaz2.y1=estrella2.centroY
    fugaz.y2=estrella.centroY-20
    fugaz1.y2=estrella1.centroY-20
    fugaz2.y2=estrella2.centroY-20
    
    estrella.centroX+=estrella.dx
    estrella1.centroX+=estrella1.dx
    estrella2.centroX+=estrella1.dx
    fugaz.centroX+=estrella.dx
    fugaz1.centroX+=estrella1.dx
    fugaz2.centroX+=estrella1.dx
    estrella.centroY+=estrella.dy
    estrella1.centroY+=estrella1.dy
    estrella2.centroY+=estrella1.dy
    fugaz.centroY+=estrella.dy
    fugaz1.centroY+=estrella1.dy
    fugaz2.centroY+=estrella1.dy
    
    sol.puntos+=1 
    if(tierra.direccion=="sentido-horario"):
        tierra.rotarÁngulo+=3
        mercurio.rotarÁngulo+=7
        venus.rotarÁngulo+=5
        marte.rotarÁngulo+=1
        
    else:
        tierra.rotarÁngulo-=3
        mercurio.rotarÁngulo-=7
        venus.rotarÁngulo-=5
        marte.rotarÁngulo-=1
        
cmu_graphics.run()



