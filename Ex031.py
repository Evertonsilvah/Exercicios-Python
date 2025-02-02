dist = float(input('Qual é a distância em Km da viagem: '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(dist))
if dist < 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(dist*0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(dist*0.45))

#Outra forma de fazer
#dist = float(input('Qual é a distância em Km da viagem: '))
#print('Você esta prestes a começar uma viagem de {}Km.'.format(dist))
#preco = dist * 0.50 if dist <= 200 else dist * 0.45
#print('E o preço da sua passagem será de R${:.2f}'.format(dist*0.45))