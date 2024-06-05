import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numero = random.randint(1, 5)
resposta = int(input('Em que número eu pensei? '))
print('PROCESSSANDO...')
sleep(3)
if numero == resposta:
    print('Você venceu, parabéns!!!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(numero, resposta))
