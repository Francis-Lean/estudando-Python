preço = float(input('Qual o preço do produto?'))
print('O produto que custava R${:.1f}, na promoção com desconto de 5% vai custar R${:.1f}.'.format(preço, preço - preço * 0.05))
