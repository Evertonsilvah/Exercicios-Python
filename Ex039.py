from datetime import date

nasc = int(input('Digite o ano de Nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    print(f'Seu alistamento será em {atual + saldo}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    print(f'Seu alistamento foi em {atual - saldo}')
else:
    print('Você precisa se alistar imediatamente.')