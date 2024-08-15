print("PRODUCIDO EN EL DIA")
litros_leche = int(input(" digite la cantidad de leche: "))

#CONVERSION DE LITROS A GOLES
conversion = litros_leche*float(3.785)

print("VALOR DEL GALON DE LECHE")
valor = int(input("Digite el valor: "))

print(" PAGO DEL PRODUCIDO EN EL DIA")
pago = valor * int(conversion)

print(f'El pago que resivio el productor por el dia producido es de ${pago} ')

