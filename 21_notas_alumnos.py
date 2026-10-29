#indica cuantos alumnos han aprobado.
notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
aprobados=0
for nota in notas_alumnos:  
    if nota>=5:
        aprobados=aprobados+1
print("El total de aprobados es ",aprobados)
#Indica la nota mas alta
nota_alta=0
for nota in notas_alumnos:  
    if nota>nota_alta:
        nota_alta=nota     
print("La nota mas alta es ",nota_alta)

