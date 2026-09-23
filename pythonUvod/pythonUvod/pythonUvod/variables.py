# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

ime = "Karlo"       #string tip podatka
brojUcenika = 24    # int tip podatka
prosjek = 4.25      # float tip podatka
polozio = True      # bool tip podatka 

print("Hello")    
print(ime)
print(brojUcenika)
print(type(brojUcenika))
print(type(prosjek))

                                              # ctrl + k + c = komentirati vise linija odjednom
                                              #  ctrl + k + u = odkomentirati vise linija odjednom


bodovi = 10

bodovi = bodovi + 2

bodovi += 5                          # isto kao (bodovi = bodovi + 5)

print(bodovi)

ime = "Ana"
Ime = "Marko"

print(ime,Ime)

x, y = 3, 7
print(x,y)


#Aritneticki operatori

a = 17
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)           # podjeli i ostaje (ispisuje) ostatak
print(a // b)          # zaokruzuje cijeli broj 
print(a % b)
print(a ** 2)
print((a + b) * 4)

#Pretvaranje tipova podataka

tekst = "25"
broj = int(tekst)
print(broj + 10)        

cijena = float("2.5")
print(cijena * 2)

print (int(4.9))      # odbacuje .9 dio ispisuje 4 jer nismo naredili da zaokruzi broj
print (float(4))      # napise broj s decimalom

print(round(4.6))     # zaokruzuje na vecu tj blizu decimalu

