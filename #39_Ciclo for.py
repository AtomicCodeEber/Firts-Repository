"""Estructura de repetición delimitada de ciertas acciones.

- ***Sintax***
    for [variable] in [objeto interable][:]
    [instrucción]
    
Un objeto iterable es aquel que permite recorrer 
sus elementos uno a uno, como lo sería una cadena de caracteres."""

# Ejemplo
# Asigna valores a una variable creada en el propio bucle
# Imprime los valores de una variable uno a uno de forma vertical
lov="Hola"
for example in lov:
    print(example)

print("Se ha terminado el proceso.")
print("\n")

# Actividad
unforgiven="Hola, tonotos"
for forgive in unforgiven:
    print(forgive)

print("The End...")
print("\n")

# Aplicación propia
x="Hola, "
x+="te perdono..."
for number in x:
    print(number)

print("The End...")