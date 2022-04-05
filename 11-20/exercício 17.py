from math import hypot
A = float(input('Digite a medida do primeiro cateto:'))
B = float(input('Digite a medida do segundo cateto:'))
print('A medida da hipotenusa do triângulo retângulos de lados {} e {} é igual a {:.2f}!'.format(A,B,hypot(A,B)))
