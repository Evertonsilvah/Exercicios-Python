salario = float(input('Qual é o salario do funcionário? R$'))

if salario <= 1250:
    nsalario = salario + (salario * 15 / 100)
else:
    nsalario = salario + (salario * 10 / 100)

print('Quem ganhava R${:.2f} para a granhar R${:.2f} agora.'.format(salario, nsalario))