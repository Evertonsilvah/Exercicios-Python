casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
parc = casa /(tempo * 12)
minimo = salario*30/100
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos, a parcela será de R${parc:.2f}')
if parc <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')