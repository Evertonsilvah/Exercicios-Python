import random
from time import sleep
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
num = int(input('Em que numero eu pensei? '))
a = 1
b = 2
c = 3
d = 4
e = 5
f = 0
print('PROCESSANDO...')
sleep(2)
lista = [a,b,c,d,e,f]
sorteado = random.choice(lista)

if num == sorteado:
    print('VOCÊ GANHOU! Eu também pensei no numero {}'.format(sorteado))
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(sorteado,num))

#Resultado do video
#from random import randint (para sortear numeros inteiros)
#from time import sleep (para o programa demorar um pouco na resposta)
#computador = randint(0,5)
#print('*-' * 20
#print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
#print('*-' * 20
#jogador = int(input('Em que numero eu pensei? '))
#print('PROCESSANDO...')
#sleep(2)
#if jogador == computador:
#print('VOCÊ GANHOU! Eu também pensei no numero {}'.format(computador))
#else:
#print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador,jogador))
