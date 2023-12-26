"""Desarrollar un programa que elimine una 
palabra que forme parte de una cadena de caracteres"""

"- La cadena tiene que ser solicitada desde el teclado"
"- La palabra a eliminar deberá ser solicitada desde teclado"

print("Sistema de erradicación de un caracter en variable string")
print("\n")
name=input("Estimado usuario, ingrese su nombre: ")
print("\n")
string=input(f"Hola, {name}, ¿Cuál es la frase seleccionada?: ")
erase=input("¿Cuál es la palabra a eliminar?: ")
índice=string.find(erase)
new=string[0:índice]+string[índice+len(erase)+1:]
print("\n")
print(new)
