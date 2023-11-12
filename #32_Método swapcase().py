# Método swapcase

"""Este método tiene la facultad de invertir el 
formato de las letras, de minúsculas o mayúsculas"""

emotion="I feel something special for Kadedi..."
print(emotion)
print(emotion.swapcase())

"Comparation with upper() and lower()"

dx="i want to know"
dy="I HATE YOU"
print(dx)
print(dy)

print(dx.upper())
print(dx.swapcase())

print(dy.lower())
print(dy.swapcase())

# Example

name=input("How do you want to be called?: ")
print(f"Hi, {name}, this is your name without swapcase method.")
print(f"And then, this is your name with that method: {name.swapcase()}")

# Example 2

title="i LOVE YOU"
title_2=", Kareri..."
print(title+title_2)

print(f"We need to change {title}, so, with the swapcase is {title.swapcase()+title_2}")