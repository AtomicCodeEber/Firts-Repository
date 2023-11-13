# This method can write the sentences in capitals in them beggining

name=input("Write your name: ")
print("Hi, {}, you have to know this".format(name))
print(name.capitalize())

# Exercise

yeah="yeAH, buDDy"
print(f"Before correctiom: {yeah}")
yeah=yeah.capitalize()
print(f"After correction: {yeah}")


"Comparación con 'title()'"

elo=input("Write a name:")
print(f"Hi, {elo}, this is your name.")
print(f"This is the correction: {elo.title()}")
