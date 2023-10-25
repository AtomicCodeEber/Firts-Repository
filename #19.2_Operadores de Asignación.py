#Existen distintos tipos de Operadores e 
#asignación, los cuales pueden ser implementados
#en texto o en valores aritméticos

print("         Cadenas de Carácteres")
name= "Hola. "
name+=input("Ingresa tu nombre: ")
texto=print("Hola,",name,)
texto+=print(", este es el incremento y decremento de una variable")
x=1
print("         Incremento o aumento.")
print("El valor inicial de 'x' es:",x)
# Conforme avanza el diagrama, el valor asignado a x aumenta 
# cada vez que se escribe el incremento y/o decremento
x+=1
x+=1
x+=1
x+=1
print("El valor final de 'x' es:",x)

print("Decremento")
print("El valor inicial de 'x' es:",x)
x-=1
x-=1
x-=1
x-=1
print("El valor final de 'x' es:",x)