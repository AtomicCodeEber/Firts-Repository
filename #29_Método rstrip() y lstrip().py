# Sustraction of text

text_1="The blade is me"
print(text_1)
text_1=text_1.rstrip("me")
print(text_1)

text_2="You gonna do it"
print(text_2)
text_2=text_2.rstrip("it")
print(text_2)

text_3="\tHola, Eber\n"
print(text_3)
text_3=text_3.rstrip("s tHol\t\n")

# lstrip()

formule="I'm stronger"
formule=formule.lstrip("I'm")
print(formule)

function=" Truth, covered in security "
function=function.lstrip("Truth")
print(function)

x="\tHola, Eber\n"
print(x)
x=x.lstrip("s tHol\t\n")
print(x)