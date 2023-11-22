
"Quizz: Derecho Constitucional Interactivo"

print("\n")
inicio="Bienvenido al cuestionario sobre el 'Derecho Constitucional'"
print(inicio.center(66,"="))
print("\n")

q_0="¿Qué es el derecho?"
print(q_0.center(26,"/"))
print("a. Ciencia social que estudia las normas que regulan a la sociedad.")
print("b. Materia académica y judicial que impone normas a seguir.")
print("c. Orden normativo que regula la conducta humana.")

laws=input("Respuesta 0: ")

if laws == "a" or laws=="c":
    print("Correcto :)")
    r0=1
else:
    print("Incorrecto :(")
    r0=0
print("\n")

q_1="El Derecho Constitucional es una rama que estudia..."
print(q_1.center(50,"/"))
print("a. La administración pública.")
print("b. Principios, Conceptos y Leyes.")
print("c. Las relaciones jurídicas entre individuos.")
print("d. Las condiciones laborales y económicas.")
definition=input("Respuesta 1: ")

"Definir cuantas preguntas se realizarán"
"Implementar un sistema"

if definition == "b":
    print("Correcto :)")
    r1=1
else:
    print("Incorrecto :(")
    r1=0
print("\n")

q_2="¿A qué clasificación pertenece el Derecho Constitucional?"
print(q_2.center(50,"/"))
print("a. Derecho Privado.")
print("b. Derecho Público.")
clasification=input("Respuesta 2: ")

if clasification == "b":
    print("Correcto :)")
    r2=1
else:
    print("Incorrecto :( ")
    r2=0
print("\n")


q_3="¿En qué partes se divide la Constitución?"
print(q_3.center(50,"/"))
print("a. Arcana, Civil y Electoral.")
print("b. Judicial, Ejecutiva y Legislativa.")
print("c. Dogmática y Orgánica.")
consticución=input("Respuesta 3: ")

if consticución == "c":
    print("Correcto :)")
    r3=1
else:
    print("Incorrecto :(")
    r3=0
print("\n")

q_4="¿Qué límites establece el Derecho Constitucional?"
print(q_4.center(60,"/"))
print("a. El control sobre el pueblo.")
print("b. El alcance que tienen las leyes.")
print("c. Restringe al poder político en la creación de normas.")
consticución=input("Respuesta 4: ")

if consticución == "c":
    print("Correcto :)")
    r4=1
else:
    print("Incorrecto :(")
    r4=0
print("\n")

q_5="¿Qué es la soberanía?"
print(q_5.center(60,"/"))
print("a. Capacidad del estado para decidir sobre asuntos internos.")
print("b. Integridad de un individuo.")
print("c. La represión y privatización de bienes.")
soberanía=input("Respuessta 5: ")

if soberanía == "a":
    print("Correcto :)")
    r5=1
else:
    print("Incorrecto :(")
    r5=0
print("\n")


"Cambiarle el número a esta pregunta y a las siguientes"

q_="¿Qué artículo estipula la función del poder legislativo?"
print(q_.center(60,"/"))
print("a. No. 45")
print("b. No. 50")
print("c. No. 72")
legislativo=input("Respuessta 2: ")

if legislativo == "b":
    print("Correcto :)")
    r=1
else:
    print("Incorrecto :(")
    r=0
print("\n")


"Parte final del código"
"Considerar hacerlo web"
"18/11/23"

answers=r0+r1+r2+r3

if answers==15 or answers==20:
    print("Felicidades, te ganaste un dulce a elegir.")
elif answers==10:
    print("Desafortunadamente reprobaste, tendrás que repasar el tema")
