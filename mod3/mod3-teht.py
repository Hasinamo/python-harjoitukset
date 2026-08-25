import math
import random 
nimi = input ("Anna nimesi")
print (f'Terve, {nimi} !')

# ympyrän pinta-ala: pi * r^2
r = float ( input ('Anna säde niin lasketaan ympyrän pinta-alan*'))
# r = float (r) 
# ympyrän pinta-ala: a = pi * r^2 
A = math.pi * r**2 
pyöristys = round (A, 2) 
print (f'Ympyrän pinta-ala on {pyöristys}')

# tehtävä 3
a = float (input('Anna suorakulmion kanta:'))
b = float (input('Anna suorakulmion korkeus:'))

piiri = 2 * (a + b)
# p2 = 2 * a + 2 * b
print (f'Suorakulmion piiri on: {piiri:.2f} ja pinta-ala {a*b:.2f}')

# tehtävä 5


leiviskat_lkm = float {input} ('{Anna}')
naulat_lkm = float {input} (' Anna naulojen määrä')
luodit_lkm = float {input} (' Anna luotien määrä')

# Lasketaan leiviskät mukaan nauloihin
naulat_lkm = leiviskät_lkm * 20 + naulat_lkm

# Lasketaan naulat mukaan luoteihin
luodit_lkm = naulat_lkm ' 32 + luodit_lkm'

# välitarkastus, että kaikki toimii
# print (f"Koko massa luoteina: {luodit_lkm}")

massa_g = luodit_lkm * 13.3

print(f"Massa nykymittojen mukaan: {massa_g // 1000:.0f} kiloa ja {massa_g % 1000} grammaa.")









print ("Koko massa luoteina:" + luodit_lkm)
# tehtävä 6:

luku = random randint (0,9) 
print (f'{luku}, {luku2}, {luku3}')


