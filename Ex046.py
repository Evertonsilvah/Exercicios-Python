from time import sleep
inicio = int(input('Digite um número para iniciar: '))
for c in range (inicio, -1, -1):
    print(c)
    sleep(1)
print(f'Fim da contagem!')