# Asignación
Texto= "Hola"
Texto +=", "
Texto +="te apesta la cola"
print(Texto)

# Concatenación
Nombre = "Eber"
Apellido = "Garcia"
Alias = "Pou"
print(Nombre,""+Apellido,""+Alias)

# Concatenación de variable int a str
number1=3
number2=5
result=number1+number2
result=str(result)
print("The Sume Result Is Equal: "+result)

# Búsqueda de Subcadenas
Message = "La existencia misma la determina uno mismo"
Search = Message.find("existencia")
print(Search)

# Extracción
Signal="Viva la Vida"
Extract= Signal[1:8]
print(Extract)

# Comparación
Message1="Pou"
Message2="Pou"
Message3="Pounecio"
print(Message1==Message2)
print(Message1==Message3)