n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media <= 5:
    print(f'A média foi {media}. Aluno REPROVADO!')
elif media <= 6.9:
    print(f'A média foi {media}. Aluno de RECUPERAÇÃO!')
else:
    print(f'A média foi {media}. Aluno APROVADO!')