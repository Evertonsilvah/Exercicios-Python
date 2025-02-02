import math

an = float(input('Digite um angulo que você deseja: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print('O angulo de {}º tem o SENO de {:.2f}, COSSENO de {:.2f} e a TANGENTE de {:.2f}.'.format(an, sen, cos, tan))
