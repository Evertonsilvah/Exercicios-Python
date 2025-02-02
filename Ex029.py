vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel - 80)*7

if vel <= 80:
    print('Parabéns! Você esta detro do limite permitido.')
else:
    print('MULTADO! Você excedeu o limite permitido, que é de 80K/h.\n Você deverá pagar uma multa de R${:.2f}!'.format(multa))

#Resolvido pelo video (condição simples)
#vel = float(input('Qual a velocidade atual do carro? '))
#if vel > 80:
#print('MULTADO! Você excedeu o limite permitido, que é de 80K/h.')
#multa = (vel - 80)*7
#print(\n Você deverá pagar uma multa de R${:.2f}!'.format(multa))

