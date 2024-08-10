print("Litros de leche producidos en un dia")
litros_leche = input(" digite la cantidad de leche: ")

#CONVERSION DE LITROS A GOLES
conversion = int(litros_leche)*float(3.785)

print("Valor de cada galon de leche")
valor = input("Digite el valor: ")

print(" Pago del producido en el dia ")
pago = int(valor) * int(conversion)

print(f'El pago que resivio el productor por el dia producido es {pago}')

