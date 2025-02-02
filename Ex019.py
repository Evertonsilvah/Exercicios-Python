import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]

print('O aluno sorteado é: {}'.format(random.choice(lista)))