import math
#Ou from math import sqrt, hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = math.sqrt(co*co + ca*ca)
#Ou hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))