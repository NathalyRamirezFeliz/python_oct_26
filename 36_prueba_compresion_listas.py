numeros=[3, -1, -9, 4, 2, 11, -8, 7, -5]
#Crea una lista a partir de la lista anterior 
# numeros que contenga solo los números positivos.

positivos = [n for n in numeros if n > 0]
print(positivos)

#SOLUCION ALTERNATIVA
# positivos = []
# for n in numeros:
#     if n > 0:
#         positivos.append(n)
# print(positivos)

#Indica si hay algun numero par en la lista
pares = [n for n in numeros if n % 2 == 0]
print(pares)