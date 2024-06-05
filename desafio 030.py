N = int(input('Me diga um número qualquer: '))
resultado = N % 2
if resultado == 0:
    print('O número {} é par!'.format(N))
else:
    print('O número {} é impar!'.format(N))
