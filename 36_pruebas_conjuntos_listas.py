dia=input("Dime un día de la semana: ")
dias={"lunes" , "martes", "miércoles"}
# dias.add("viernes")

if dia in dias:
    print("El día está en el diccionario")
else:
    print("El día no está en el diccionario")
print(dias)
# 

lista_dias=list(dias)
print(lista_dias)

listas_numeros=[4,7,11,3,2,11,9,4,7]
conjunto_numeros=set(listas_numeros)
print(conjunto_numeros)