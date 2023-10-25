# Sistema de Conversión de Número a Texto y Viceversa

print("         Menú de Opciones")

print("Presiona 1 para Convertir un Número a Palabra.")
print("Presiona 2 para Convertir una Palabra a Número.")

option=int(input("Seleccione una Opción: "))

if option==1:
    print(" Conversor de int a str.")
    number_text=int(input("Ingrese el Número deseado: "))
    if number_text==1:
        print("uno.")
    elif number_text==2:
        print("dos.")
    elif number_text==3:
        print("tres.")
    elif number_text==4:
        print("cuatro.")
    elif number_text==5:
        print("cinco.")
    else:
        print("El Número No Está Registrado.")
elif option==2:
    print(" Conversor de str a int.")
    text_number=input("Registre el Número Textualizado para su Conversión: ")
    text_number=text_number.lower()
    if text_number=="uno":
        print("1")
    elif text_number=="dos":
        print("2")
    elif text_number=="tres":
        print("3")
    elif text_number=="cuatro":
        print("4")
    elif text_number=="cinco":
        print("5")
    else:
        print("El Texto No Está Registrado.")
else:
    print("El Dígito Ingresado no es Admisible.")