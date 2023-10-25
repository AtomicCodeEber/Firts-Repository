# Programa para determinar el número mayor entre 3 dígitos ingresados.

print("         Número Mayor")
num_1=float(input("Ingrese el primer dígito: "))
num_2=float(input("Ingrese el segundo número: "))
num_3=float(input("Ingrese el tercer número: "))

if num_1>num_2 and num_1>num_3:
    print("El número",num_1,"es mayor a",num_2,"y",num_3)
else:
    if num_2>num_1 and num_2>num_3:
        print("El número",num_2,"es mayor a",num_1,"y",num_3)
    else:
        print("El número",num_3,"es mayor a",num_1,"y",num_2)