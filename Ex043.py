peso = float(input('Informe o peso: (Kg) '))
altura = float(input('Informe a altura: (m) '))
imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('Você esta abaixo do peso.')
elif imc <= 25:
    print('Você esta no seu peso ideal')
elif imc <= 30:
    print('Você esta sobrepeso')
elif imc <= 40:
    print('Você esta obeso.')
else:
    print('Você esta com Obesidade Mórbida')