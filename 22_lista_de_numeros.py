#Solicitar la introduccion de numeros, uno a uno Y
# después y los guardamos en una lista.
# Después pedir un número, pregunta si quiere 
# introducir otro número si dice sí (S), pide uno 
# nuevo y asi sucesivamente hasta que diga
# NO (N) al final muestra la lista completa
resp="s"
lista=[]
while resp=="s" or resp=="S":
    try:
        num=int(input("Introduce un número:"))
        lista.append(num)
        resp=input("Desea Introducir otro número (S/N)")
    except ValueError:
        print("No es un valor númerico, vuelve a intentar")
print(f"La lista es :{lista}")

    