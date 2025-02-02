cont = 0
soma = 0
for n in range (1,501,2):
    if n % 3 == 0:
        cont += 1
        soma += n
print(f'A soma de todos os {cont} valores solicitados é igual a {soma}')