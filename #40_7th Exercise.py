"""Desarrollar un programa que invierta una 
cadena de caracteres seleccionada por el usuario """

"- No se permite modificar la cadena original."
"- Utilizar el ciclo for"

# Comienzo del código

begin="Programa de inversión de caracteres"
print(begin.center(len(begin)+10, "/"))
print("\n")

name=input("¿Cuál es tu nombre?: ")
sdg2=input(f"Hola, {name}, ingresa la palabra a invertir: ")
print("\n")

print(sdg2)

for invert in sdg2:
    sdg2_invert=invert+sdg2

print(sdg2_invert)