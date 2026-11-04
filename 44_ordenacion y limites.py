lista=[5,2,11,6,44,20,1]
lista_ordenada=sorted(lista,reverse=True)
print(lista_ordenada)
nombres=["bicicleta","oro","casa","martillo","coche"]
print(sorted(nombres))

#ordenación personalizada, por ejemplo por numero de caracteres
nombres_ordenados=sorted(nombres,key=len)
print(nombres_ordenados)