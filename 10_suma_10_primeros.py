#Hacer un programa que muestre de la suma de los 10 primeros numeros naturales
#numeros naturales entre 1 y un número leido por telcado

# suma:int=0
suma=0
numero=int(input("Introduce numero: "))
for num in range (1,numero):
    suma=suma+num
    print("la suma de los números es", suma)
