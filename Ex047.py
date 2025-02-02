for n in range (1,51):
    print('.', end="")
    if n % 2 == 0:
        print(n, end=' ')
print('\nFim do primeiro "for"')

# OU PODE SER FEITO DA SEGUINTE FORMA (DIMINUI A QUANTIDADE DE LAÇOS/ITERAÇÕES):

for c in range (2, 51, 2):
    print('.', end="")
    print(c, end=" ")
print('\nFim do segundo "for"')

#O resultado é o mesmo, mas da segunda forma, o programa processa menos vezes.