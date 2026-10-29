#Lee la nota de un almuno y dependiendo del numero (0 -10)
#le indica si es suspenso  (menos de 5), aprobado (5 o 6 ),
#notable (7u 8) ó sobresaliente (9 o 10)

# num=int(input("Introduce un número:"))

# if num<5:
#     print ("suspenso")
# elif num>=5 and num<=6:
#     print("aprobado")
    
# elif num>=7 and num<=8:
#     print("notable")

# elif num>=9 and num<=10:
#     print("notable")

# else: 
#     print("Nota no valida")
    

nota=int(input("Introduce nota: "))
match nota:
    case 0|1|2|3|4:
        print("Estás suspenso")
    case 5|6:
        print("Estás aprobado")
    case 7|8:
        print("Tienes un notable")
    case 9|10:
        print("Tienes un sobresaliente")
    case _:
        print("Nota no válida") 

