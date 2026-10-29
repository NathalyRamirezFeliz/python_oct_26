#solicita la introducción de una contraseña, si es correcta
#le dice que es un usuario válido. Si no es correcta, se le vuelve a pedir.
#Así, hasta tres intentos. Si después del tercer intento la contraseña es incorrecta
#le dice que no es un usuario válido

# password = "admin"
# intentos = 3
# acertado = False

# while intentos > 0 and acertado == False:
#     contra = input("Introduce una contraseña: ")
#     if contra == password:
#         acertado = True
#         print("Contraseña correcta")
#     else:
#         intentos -= 1
#         print("Contraseña incorrecta, vuelve a intentar")

# if acertado == False:
#     print("No es un usuario válido")

password="admin"
intentos=3
acierto=False
while intentos>0 and acierto==False:
    contra=input("Introduce contraseña ")
    if contra==password:
        acierto=True
        print("Usuario válido!")
        break
    else:
        print("Vuelve a intentar!")
        intentos=intentos-1
    if not acierto: #and intentos==0:
        print("Usuario no válido!")