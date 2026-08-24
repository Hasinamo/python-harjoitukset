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




tehtävä 6:

luku = random randint (0,9) 
print (f'{luku}, {luku2}, {luku3}')


