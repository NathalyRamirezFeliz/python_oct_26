#Al iniciar el programa se debe mostrar el siguiente menú: 
# 1.-Añadir nota  
# 2. -Mostrar notas extremas 
# 3.-Total de aprobados 
# 4.Nota media 
# 5-Mostrar todas  
# 6. Salir
#El usuario elige una opción (1-6)
# y el programa le muestra o pide los
# datos necesarios para llevar a cabo la acción. 
# Después, vuelve a salir el menú y así hasta que elija salir.


opcion_elegida = 0

notas = []
mayor=0
# menu = ["1.- Añadir nota", "2.- Mostrar notas extremas", 
#         "3.- Total de aprobados", "4.- Nota media", 
#         "5.- Mostrar todas", "6.- Salir"]
while opcion_elegida != 6:
    print("Introduce un número del 1 al 6")
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
    
    opcion_elegida = int(input("Elige una opción: "))
    
    match opcion_elegida:
        case 1:
            notas.append(int(input("Introduce la nota: ")))
        case 2:
            if notas:
                print(f"Nota máxima {max(notas)}")
                print(f"Nota mínima {min(notas)}")
            else:
                print("No hay notas para mostrar")
        case 3:
            aprobados = 0
            for nota in notas:  
                if nota>=5:
                    aprobados=aprobados+1
            print("El total de aprobados es ",aprobados)
        case 4:
            suma = 0
            for nota in notas:
                suma += nota
            if len(notas) == 0:
                print("No hay notas para calcular la media")
            else:
                print(f"La nota media es {suma/len(notas)}")
        case 5:
            print("Las notas son: ", notas)
        case 6:
            print("Fin del programa...")
        case _:
            print("Opción no válida, elige un número del 1 al 6")
            
        
            
            
# ####  
#     if opcion_elegida == 1:
#         print("Has elegido añadir nota")
#         nota = float(input("Introduce la nota: "))
#         notas.append(nota)
#         print("Nota añadida correctamente")
# ######    
#     elif opcion_elegida == 2:
#         print("Has elegido mostrar notas extremas")
#         if notas:
#             print(f"Nota máxima: {max(notas)}")
#             print(f"Nota mínima: {min(notas)}")
#             print(f"Las notas en orden son: {sorted(notas,reverse=True)}")
#         else:
#             print("No hay notas para mostrar")
# ######3
#     elif opcion_elegida == 3:
#         print("Has elegido Total de aprobados")
#         aprobados = 0
#         for nota in notas:  
#             if nota>=5:
#                 aprobados=aprobados+1
#             print("El total de aprobados es ",aprobados)
#     else:
#             print("No hay notas para mostrar")
# #####
