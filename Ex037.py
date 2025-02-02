num = int(input('Digite um número inteiro: '))
print(
    '''
    [1] converter para BINÁRIO
    [2] converter para OCTAL
    [3] converter para HEXADECIMAL
    '''
)
escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'O número {num} em Binário é {bin(num)[2:]}')
elif escolha == 2:
    print(f'O número {num} em Octal é {oct(num)[2:]}')
elif escolha == 3:
    print(f'O numero {num} em Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção invalida! Tente novamente.')