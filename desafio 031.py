D = float(input('Qual a distâcia da viagem em Km? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(D))
if D <= 200:
    print('O valor da passagem será R${:.2f}'.format(D * 0.50))
else:
    print('O valor da passagem será R${:.2f}'.format(D * 0.45))

