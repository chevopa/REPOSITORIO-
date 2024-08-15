print("AREA RECTANGULO")
baseRectangulo = int(input(" Ingrese la longitud de la base : "))
alturaRectangulo = int(input(" Ingrese la altura : "))
area_rectangulo = int(baseRectangulo)*int(alturaRectangulo)
print(f'la area del rectangulo ese de {area_rectangulo} mt')

print("AREA TRIANGULO")
baseTriangulo = int(input(" Ingrese la longitud de la base : "))
alturaTriangulo = int(input(" Ingrese la altura : "))
area_triangulo = baseTriangulo*alturaTriangulo/2
print(f'la area del triangulo ese de {area_triangulo} mt')

print("AREA TERRENO")    
area_terreno = area_triangulo + alturaRectangulo
print(f'la area del terreno ese de {area_terreno} mt')