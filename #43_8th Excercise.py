"""Desarrollar un programa que muestre la tabla de multiplicas
de un número ingresado

- Ciclo for
- Multiplicaciones de 0 a 10"""

welcome="Calculadora de tablas de multiplicar"
print(welcome.center(len(welcome)+10,"/"))
print("\n")

name=input("Ingresa tu nombre: ")
number=int(input(f"Hola, {name}, ingresa el número a multiplicar: "))

for tab in range (0,number*11,number):
    x=0
    print(x,"*", number,"=",tab)
    x=x+1