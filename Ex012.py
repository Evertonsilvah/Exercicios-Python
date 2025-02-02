preco = float(input('Qual é o valor do produto? R$'))
porc = int(input('O cliente terá quantos porceto (%) de desconto? '))
npreco = preco - (preco * porc / 100)

print('O produto custava {}, na promoção com o desconto de {}% vai custar {:.2f}.'.format(preco, porc, npreco))