#Solicita un programa que solicite la introduccion de un 
# numero despues, muestra todos los pares entre 1 y ese número

num=int(input("Introduce un número: "))
for n in range(1,num+1):
        if n%2==0:
                print(n,"Es par")
        
