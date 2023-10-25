"Asignación de Promedios en Base a Calificaciones escolares"

name=input("What's Your Name? ")
math=float(input("Ingresa tu calificación de 'Matemáticas': "))
biology=float(input("Ingresa tu calificación de 'Biología': "))
chemestry=float(input("Ingresa tu calificación de 'Química': "))

promedio=(math+biology+chemestry)/3

if promedio>=6:
    print("Felicidades,",name,"aprobaste con: ",round(promedio,2))
else:
    print(name,", desafortunadamente reprobaste con: ",round(promedio,2))