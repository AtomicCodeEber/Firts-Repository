# Este método es capaz de contar la cantidad de repeticiones de un dato

"""A diferencia del método len, determina la cantidad, 
no las posiciones de los carácteres"""

# Conteo

string="Hola mundo"
print(string.count(""))
print(len(string))

# Ubicación y conteo.
# Diferencia letras mayúsculas y minúsculas, al igual que acentos.
# Toma en cuenta las frases enteras como un solo término.
# Realiza el conteo de unidad en unidad

mom="mi mamá me mima"
print(mom.count("m"))
print(mom.count("M"))
print(mom.count("mi mamá"))
print(len(mom))

# Dos argumentos
# El primer argumento determina el comienzo del recorrido
# El segundo asigna el límite de conteo

print(mom.count("m", 3))
print(mom.count("m", 3, 4))

# Argumento negativo
"""Los números negativos representan el 
comienzo para el argumento desde la derecha, yendo
de izquierda a derecha"""

print(mom.count("m", -3))
print(mom.count("m", -3, -1))