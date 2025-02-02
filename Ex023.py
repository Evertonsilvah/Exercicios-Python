#Como eu fiz (Errado: Se colocar menos que 4 digitos, não funciona. Seria necessário utilizar condições (Se))
"""num = str(input('Digite um numero: '))
print('Analisando o numero {}...'.format(num))

print('Unidade: {}'.format(num[3]))
print('Dezena:  {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar:  {}'.format(num[0]))"""

#Resposta do video
num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))