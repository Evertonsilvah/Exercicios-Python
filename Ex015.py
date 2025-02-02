dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos KMs rodados: '))
valor = (dias*60) + (km*0.15)

print('O total a pagar é R${:.2f}'.format(valor))