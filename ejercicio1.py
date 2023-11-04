from cmu_graphics import*
cristianismo = 2300
islam = 1900
hinduismo = 1200
budismo = 520 
religionesTradicionalesChina = 394
religionesAfroamericanas = 100
personasNoReligiosas = 1200

sumaDeReligiones= cristianismo + islam + hinduismo + budismo + religionesTradicionalesChina+ religionesAfroamericanas+ personasNoReligiosas
print(sumaDeReligiones)
porcentaje1 = (cristianismo /sumaDeReligiones)
porcentaje2 = (islam /sumaDeReligiones)
porcentaje3 = (hinduismo /sumaDeReligiones)
porcentaje4 = (budismo /sumaDeReligiones)
porcentaje5 = (religionesTradicionalesChina /sumaDeReligiones)
porcentaje6 = (religionesAfroamericanas /sumaDeReligiones)
porcentaje7 = (personasNoReligiosas /sumaDeReligiones)

porcentajeGrafico1 = int(porcentaje1*100)
porcentajeGrafico2 = int(porcentaje2*100)
porcentajeGrafico3 = int(porcentaje3*100)
porcentajeGrafico4 = int(porcentaje4*100)
porcentajeGrafico5 = int(porcentaje5*100)
porcentajeGrafico6 = int(porcentaje6*100)
porcentajeGrafico7 = int(porcentaje7*100)

print(porcentajeGrafico1)
print(porcentajeGrafico2)
print(porcentajeGrafico3)
print(porcentajeGrafico4)
print(porcentajeGrafico5)
print(porcentajeGrafico6)
print(porcentajeGrafico7)

anguloDeBarrido1= int(porcentaje1*360)
anguloDeBarrido2= int(porcentaje2*360)
anguloDeBarrido3= int(porcentaje3*360)
anguloDeBarrido4= int(porcentaje4*360)
anguloDeBarrido5= int(porcentaje5*360)
anguloDeBarrido6= int(porcentaje6*360)
anguloDeBarrido7= int(porcentaje7*360)

print(porcentaje1)
print(porcentaje2)
print(porcentaje3)
print(porcentaje4)
print(porcentaje5)
print(porcentaje6)
print(porcentaje7)

print(anguloDeBarrido1)
print(anguloDeBarrido2)
print(anguloDeBarrido3)
print(anguloDeBarrido4)
print(anguloDeBarrido5)
print(anguloDeBarrido6)
print(anguloDeBarrido7)

Circle(130,240,120)
arco1=Arc(130,240,240,240,0,anguloDeBarrido1,fill="azul")
arco2=Arc(130,240,240,240,108,anguloDeBarrido2,fill="rojo")
arco3=Arc(130,240,240,240,197,anguloDeBarrido3,fill="verde")
arco4=Arc(130,240,240,240,253,anguloDeBarrido4,fill="oro")
arco5=Arc(130,240,240,240,277,anguloDeBarrido5,fill="cian")
arco6=Arc(130,240,240,240,295,anguloDeBarrido6,fill="lima")
arco7=Arc(130,240,240,240,299,anguloDeBarrido7,fill="naranja")

Rect(260,40,10,10,fill="azul")
Rect(260,60,10,10,fill="rojo")
Rect(260,80,10,10,fill="verde")
Rect(260,100,10,10,fill="oro")
Rect(260,20,10,10,fill="cian")
Rect(260,120,10,10,fill="lima")
Rect(260,140,10,10,fill="naranja")

Rotulo("cristianismo",310,42)
Rotulo("islam",310,62)
Rotulo("hinduismo",310,82)
Rotulo("budismo",310,102)
Rotulo("TradicionalesChina",330,22)
Rotulo("Afroamericanas",320,122)
Rotulo("personasNoReligiosas",338,142)
Rotulo(porcentajeGrafico1,175,200,tamaño=25)
Rotulo("%",200,200,tamaño=25)
Rotulo(porcentajeGrafico2,158,298,tamaño=25)
Rotulo("%",180,298,tamaño=25)
Rotulo(porcentajeGrafico3,76,293,tamaño=25)
Rotulo("%",98,293,tamaño=25)
Rotulo(porcentajeGrafico4,30,248,tamaño=25)
Rotulo("%",50,248,tamaño=25)
Rotulo(porcentajeGrafico5,35,216,tamaño=25)
Rotulo("%",55,216,tamaño=20)
Rotulo(porcentajeGrafico6,5,150,tamaño=15)
Rotulo("%",15,150,tamaño=15)
Rotulo(porcentajeGrafico7,80,172,tamaño=25)
Rotulo("%",103,172,tamaño=25)
Linea(27,186,15,161,finalDeFlecha=True,anchuraDeLinea=1)

Rotulo("Porcentaje Poblacional",120,40,tamaño=20)
Rotulo("En Cuanto a Religiones",120,70,tamaño=20)

cmu_graphics.run()
