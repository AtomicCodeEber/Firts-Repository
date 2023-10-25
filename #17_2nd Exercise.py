# Segundo Ejercicio Práctico

print("     =============================")
print("     Determinar El Tipo de Número")
print("     =============================")

number=int(input("Introduzca un valor entero: "))
number_2=2

if number%number_2==0:
    print("El número",number,"es un Par.")
elif number%number_2==1:
    print("El número",number,"es Impar")