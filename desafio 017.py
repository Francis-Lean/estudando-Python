from math import hypot
print('Calcule a hipotenusa do triângulo retângulo')
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hipotenusa = hypot(co, ca)
print('o comprimento da hipotenusa deste triângulo retângulo equivale à {:.2f}.'.format(hipotenusa))
