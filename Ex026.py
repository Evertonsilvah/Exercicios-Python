#Como eu fiz
frase = str(input('Digite uma frase: ')).strip()

print('A letra A aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.lower().find('a')+1))
print('A ultuma letra A apareceu na posição {}'.format(frase.lower().rfind('a')+1))

#Observação
#Adicionado o "+1" pois o sistema irá contar 0123 e não 123.
#Se a palavra inicia com A o sistema apresentaria a posição 0. Soma-se mais 1 para que o usuário veja a conta sem o 0