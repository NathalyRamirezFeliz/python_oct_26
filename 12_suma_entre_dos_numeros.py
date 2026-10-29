# Solicita la introducción de dos números y calcula la suma de
# todos los números comprendidos entre el menor y el mayor


#PRIMERA SOLUCION
# numero1 = int(input("Introduce número: "))
# numero2 = int(input("Introduce un segundo número: "))
# suma = 0
# for num in range(min(numero1, numero2), max(numero1, numero2) + 1):
#     suma += num
# print("La suma de los números comprendidos entre ambos es:", suma)


##SEGUNDA SOLUCION
# # numero1 = int(input("Introduce primer número: "))
# numero2 = int(input("Introduce un segundo número: "))
# suma = 0
# if numero1 < numero2:
#     for num in range(numero1, numero2 + 1):
#         suma += num
# else:
#     for num in range(numero2, numero1 + 1):
#         suma += num
# print("La suma es:", suma)

#TERCERA SOLUCION
# suma=0
# numero1 = int(input("Introduce primer número: "))
# numero2 = int(input("Introduce un segundo número: "))

# if numero1 < numero2:
#     menor=numero1
#     mayor =numero2
# else:
#     menor=numero2
#     mayor=numero1
    
#     for n in range(menor, mayor+ 1):
#         suma=suma+n 

# print("La suma es:",suma)

#CUARTA SOLUCION
suma=0
numero1 = int(input("Introduce primer número: "))
numero2 = int(input("Introduce un segundo número: "))

if numero1>numero2:
   numero1,numero2=numero2,numero1
    
for n in range(numero1,numero2+1):
        suma=suma+n 

print("La suma es:",suma)