cursos=["Java","Python","TypeScript","C","Dart"]
#Pregunta al usuario quelenguaje quiere aprender, y el 
# programa le indicará si existe un curos 
# para ese lenguaje o no

lenguaje=input("Que lenguaje quieres aprender? ")
if lenguaje in cursos:
    print("Si tenemos un curso de", lenguaje)
else:
    print("No tenemos un curso de", lenguaje)
    
