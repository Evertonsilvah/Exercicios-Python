from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''
Suas opções:

[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('*=' * 15)
print(f'Computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('*=' * 15)

if computador == 0: #PEDRA
    if jogador == 0: #PEDRA
        print('EMPATE')
    elif jogador == 1: #PAPEL
        print('VOCÊ VENCEU')
    elif jogador == 2: #TESOURA
        print('COMPUTADOR GANHOU')
    else:
        print( 'Jogada inválida')

if computador == 1: #PAPEL
    if jogador == 0: #PEDRA
        print('COMPUTADOR GANHOU')
    elif jogador == 1: #PAPEL
        print('EMPATE')
    elif jogador == 2: #TESOURA
        print('VOCÊ VENCEU')
    else:
        print('Jogada inválida')

if computador == 2: #TESOURA
    if jogador == 0: #PEDRA
        print('VOCÊ GANHOU')
    elif jogador == 1: #PAPEL
        print('COMPUTADOR GANHOU')
    elif jogador == 2: #TESOURA
        print('EMPATE')
    else:
        print('Jogada inválida')