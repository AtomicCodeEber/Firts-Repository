# Sentencias Condicionales

"Condicionales Simples"

print("     Medio para la Captura de Datos de Calificaciones")

name=input("What's Your Name? ")
math=int(input("Ingrese el promedio de 'Matemáticas': "))
chemestry=int(input("Ingrese el promedio de 'Química': "))
biology=int(input("Ingrese el promedio de 'Biología': "))

if math>=6:
        print(name,".","Has Aprobado Matemáticas con:",math)

if math<=5:
        print(name,".","Desafortunamente Has Reprobado con:",math)

if chemestry>=6:
        print(name,".","Has Aprobado Química con:",chemestry)

if chemestry<=5:
        print(name,".","Desafortunamente Has Reprobado Química con:",chemestry)

if biology>=6:
        print(name,".","Has Aprobado Biología con:",biology)

if biology<=5:
        print(name,".","Desafortunadamente Has Reprobado Biología con:",biology)

promedio=(math+chemestry+biology)/3

print(name,".","Tu Promedio Es Equivalente A:",promedio)