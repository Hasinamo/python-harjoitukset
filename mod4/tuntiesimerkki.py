#  Tuntiesimerkkejä moduuliin 4

import random

## kolikomheittosimulaattori
random_number = random.randint (0,1)
print (random_number)

# if lauseen_ehto_muodostuu AINA True tai False arvoksi
if random_number == 0:
    result = "krunaa"
    print ("kruuna tuli")
else:
     result = "klaava"

if random_number == 1:
      result = "klaava"

 print (f"Heitit kolikkoa ja sait {result}n.")

# booleon 
onko_totta = True
if onko_totta:
     print("Onko se totta!")




print


# kolikonheittosimulaattori 2.0
random_number = random.random()
print (random_number) # liukulukuarvo väliltä 0-1

# Kolikko jää pystyyn todennäköisyys 1/1000
if random_number < 0.01:
     print ("Kolikko jää pystyyn")
elseif random_number < 0.505:
    print ("Krunaa tuli.")
else:
    print ("Klaava tuli")

## erilaisia ehtoja

print ("matti" <= "matti")

     arvo = 150

print( 90 < arvo < 110 )
print (100 != 101)

# kalvoesimerkki

ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))

if (ikä >= 18 or ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")

print (True or (True and False )

# esimerkki ehdoista, kun jälkimäinen if-lause ikäarvolla 18
#print(True or (True and False)

print(not True)