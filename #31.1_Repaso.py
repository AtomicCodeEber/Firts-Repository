# Repaso de las últimas 7 lecciones

"Función len"

d_drop="El roce de la locura es suficiente para la desdicha"
print("La longitud de la variable es equivalente a: {}".format(len(d_drop)))

"Concatenación Fomat"

name=input("What's your name?: ")
food=int(input("How many times do you eat at day?: "))

print("The user {0} eat {1} time(s) at day.".format(name,food))

"Concatenación fstrings"

bankai=int(input("What's the sum of 18 and 12: "))

if bankai==30:
    print(f"The result was: {bankai}")
else:
    print("You're wrong...")