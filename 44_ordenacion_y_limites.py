lista=[5,2,11,6,44,20,1]
lista_ordenada=sorted(lista,reverse=True)
print(lista_ordenada)
nombres=["bicicleta","oro","casa","martillo","coche"]
print(sorted(nombres))

#ordenación personalizada, por ejemplo por numero de caracteres
# nombres_ordenados=sorted(nombres,key=len)
# print(nombres_ordenados)

print(sorted(nombres,key=lambda e:len(e)))

#de la lista de números, imprime el mayor.

print(max(lista))

#imprimir el menor de la lista de  nombres

print(min(nombres))

#Imprime el que tiene menos caracteres.

print(min(nombres,key=lambda e:len(e)))
