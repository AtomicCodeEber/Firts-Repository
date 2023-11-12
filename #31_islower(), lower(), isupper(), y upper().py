"""Estos métodos están pensados para 
cambiar la categoría de una variable Atring"""

# islower () and lower ()

'Lower'

poem="Resuena el estruendo, la serenidad ha sido mermada."
print(poem.islower())
poem=poem.lower()
print(poem)

'Upper'

verse="Oscurece tu brillo, para renacer más candente."
print(verse.isupper())
verse=verse.upper()
print(verse)

"Ejercicio 1"
text=input("Introduce a text: ")

print(f"\nAll the letters are capitals?: {text.islower()}")
text=text.lower()
print(f"Edited Version: {text}")

"Ejercicio 2"

print(f"\nAll the letters are capitals?: {text.isupper()}")
print(f"Edited Version: {text.upper()}")

print(f"Original Text: {text}")


'Comparación con istitle() y title()'

# istitle y title

stella="i LOve You vERy muCH"
print(stella.istitle())
print(stella)
print(stella.title())