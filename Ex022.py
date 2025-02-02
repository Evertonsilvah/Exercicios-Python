nome = str(input('Digite o seu nome completo: ')).strip()
print('O nome digitado é: ',nome)

print('Em letras maiúsculas: ',nome.upper())

print('Em letras minúsculas: ',nome.lower())

#Como eu fiz (Contou um caractere a mais)
#dividido = nome.split()
#print('O nome digitado possui {} letras.'.format(''.join(dividido).count('')))

#Resposta do video
print('Seu nome te ao todo {} letras'.format(len(nome) - nome.count(' ')))

#Como eu fiz (Contou um caractere a mais)
#div = nome.split()
#print('O primeiro nome tem {} letras.'.format(div[0].count('')))

#Resposta do video
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#Outra forma
#separa = nome.split()
#print('Seu primeiro nome tem {} letras'.format(len(separa[0])))