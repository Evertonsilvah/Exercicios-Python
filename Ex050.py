soma = 0
cont = 0
for n in range(1,7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 0:
    print('Não foram digiados números pares.')
elif cont == 1:
    print(f'Apenas o numero {soma} é Par.')
else:
    print(f'Foram digitados {cont} números pares. A soma desses números é: {soma}')