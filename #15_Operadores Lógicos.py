"Conjunción"

num_1= float(input("Ingrese un Número Mayor a 2 y Menor a 5: "))
num_2=float(input("Ingrese un Número Mayor o Igual a 6: "))
num_3=float(input("Ingrese un Número Igual a 3: "))

if num_1>2 and num_1<5:
    print("El número",num_1, "es mayor a 2 y menor a 5.")
else:
    print("El número no cumple las condiciones")

if num_2>6 or num_2==6:
    print("El número",num_2,"es mayor o igual a 6.")
else:
    print("El número no cumple con ninguna de las dos condiciones.")

if not num_3==3:
    print("Se ha cumplido la función: El número",num_3,"no es igual a 3")
else:
    print("Noe ha cumplido la condición;",num_3,"el número es igual a 3")