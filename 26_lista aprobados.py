numeros=[4,3,7,8,7,9,2]
#Dada esa lista de notas, crea otra lista que contenga
# solo los aprobados. ademas, le añadiras un punto extra
# a cada uno. Finalmente imprime la lista.

aprobados = [nota + 1 for nota in numeros if nota >= 5]
print(aprobados)