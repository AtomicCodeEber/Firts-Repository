"""Desarrollar un programa que elimine una 
palabra que forme parte de una cadena de caracteres"""

"- La cadena tiene que ser solicitada desde el teclado"
"- La palabra a eliminar deberá ser solicitada desde teclado"

name=input("¿Cuál es tu nombre?: ")
print("\n")
phrase=input(f"Hola, {name}, ingresa la frase escogida: ")
word=input("Ingrese la palabra seleccionada: ")

if phrase.count(word) == 0:
    print("\n")
    print("Error, por favor escoja otra palabra a eliminar.")
elif phrase.count(word)!=0:
    índice=phrase.find(word)
    new=phrase[0:índice]+phrase[índice:len(word)+1]
    print("\n")
    print(new)