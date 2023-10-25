
"Se solicitará el Nombre, Clave y Antigüedad del trabajador"

print("         Derecho a Vacaciones")

name=input("Nombre del Empleado: ")
clue=int(input("Clave del Departamento del Trabajador: "))
antiquity=float(input("Años de Servicio del Trabajador: "))

if clue==1:
    print("     El empleado tiene la clave:",clue)
    if antiquity==1 and antiquity<2:
        print("El trabajador",name,"tiene derecho a 6 días de vacaciones.")
    elif antiquity>=2 and antiquity<=6:
        print("El empleado",name,"tiene derecho a 14 días de vacaciones.")
    elif antiquity>=7:
        print("El trabajador",name,"tiene derecho a 20 días de vacaciones.")
    else:
        print("El empleado",name,"no tiene derecho a vacaciones.")
elif clue==2:
    print("     El empleado",name,"tiene la clave:",clue)
    if antiquity==1 and antiquity>2:
        print("El trabajador",name,"tiene derecho a 7 días de vacaciones.")
    elif antiquity>=2 and antiquity<=6:
        print("El trabajador",name,"tiene derecho a 15 días de vacaciones.")
    elif antiquity>=7:
        print("El trabajador",name,"tiene derecho a 22 días de vacaciones.")
    else:
        print("El empleado",name,"no tiene derecho a vacaciones.")
elif clue==3:
    print("     El empleado",name,"tiene la clave:",clue)
    if antiquity==1 and antiquity<2:
        print("El trabajador",name,"tiene derecho a 10 días de vacaciones.")
    elif antiquity>=2 and antiquity<=6:
        print("El trabajador",name,"tiene derecho a 22 días.")
    elif antiquity>=7:
        print("El empleado",name,"tiene derecho a 30 días de vacaciones.")
    else:
        print("El trabajador",name,"no tiene derecho a vacaciones.")
else:
    print("Ingrese un dígito registrado.")