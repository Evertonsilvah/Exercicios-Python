salario = float(input('Informe o salário do funcionário: R$'))
porc = int(input('O salário será aumentado em quantos porcento (%)? '))

nsalario = salario + (salario * porc/100)

print('Um funcionário que ganhava R${}, com {}% de aumento, passa a ganhar R${:.2f}'.format(salario, porc, nsalario))