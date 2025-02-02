print('===== STUDIO JÉ CAPRICHO  =====')
valor = float(input('Valor da unha: '))
print('''
FORMAS DE PAGAMENTO
[1] à vista dinheiro/pix/débito
[2] à vista no credito
[3] 2x no credito
[4] 3x ou mais no credito
''')
escolha = int(input('Digite sua opção: '))

if escolha == 1:
    nvalor = valor - (valor * 10 / 100)
    print(f'Nesta forma de pagamento o valor será R${nvalor:.2f} | (10% de desconto)')
elif escolha == 2:
    nvalor = valor - (valor * 5 / 100)
    print(f'Nesta forma de pagamento o valor será R${nvalor:.2f} | (5% de desconto)')
elif escolha == 3:
    parc = valor / 2
    print(f'Não haverá descontos no valor de {valor:.2f} e cada parcela terá o valor de R${parc:.2f}.')
elif escolha == 4:
    nvalor = valor + (valor * 20 / 100)
    print(f'Nesta forma de pagamento o valor total será R${nvalor:.2f} | (20% de juros)')
    qtde = int(input('Digite a quantidade de parcelas: '))

    if qtde == 3:
        nvalor = nvalor / 3
        print(f'Cada parcela terá o valor de R${nvalor:.2f}')
    elif qtde == 4:
        nvalor = nvalor / 4
        print(f'Cada parcela terá o valor de R${nvalor:.2f}')
    elif qtde == 5:
        nvalor = nvalor / 5
        print(f'Cada parcela terá o valor de R${nvalor:.2f}')
    else:
        print('Opção invalida.')

else:
    print('Opção invalida. Volte do inicio.')