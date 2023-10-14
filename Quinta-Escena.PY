from cmu_graphics import *
#klk
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
#Contenedor de basura
Rect(0, 50, 70, 70, relleno='verdeOscuro', borde='negro')
Linea(0, 50, 74, 50, anchuraDeLinea= 3)
Linea(3, 70, 70, 70, relleno='blanco', anchuraDeLinea=14)
Rotulo('BASURA', 37, 70)
#Cubo de basura
Poligono(350, 135, 362, 184, 390, 184, 396, 135, relleno='gris', borde='negro')
Poligono(350, 135, 361, 144, 385, 144, 396, 135, relleno='grisPizarra', borde='negro')
#Alcantarilla
Poligono(115, 149, 128, 149, 122, 190, 103, 189, relleno='grisPizarraOscuro')
Linea(126, 157, 112, 157)
Linea(125, 166, 111, 166)
Linea(124, 176, 108, 176)
Linea(115, 149, 128, 149)
Linea(128, 149, 122, 190)
Linea(122, 190, 103, 189)
#Señora
Circulo(25, 154, 13)
Linea(25, 154, 25, 214)
Linea(24, 174, 36, 187)
Linea(26, 174, 12, 187)
Poligono(25, 194, 11, 214, 39, 214)
Linea(20, 211, 20, 222)
Linea(30, 211, 30, 222)
Circulo(25, 140, 5)
##Texto
Rotulo('Al fin', 55, 139)
Rotulo('arreglaron', 67, 148)
Rotulo('la carretera', 79, 157)
Rotulo('5',385, 10, tamaño=20)
#brillitos
Estrella(100, 333, 3, 4, relleno='blanco')
Estrella(254, 169, 3, 4, relleno='blanco')
Estrella(175, 36, 3, 4, relleno='blanco') 

cmu_graphics.run()