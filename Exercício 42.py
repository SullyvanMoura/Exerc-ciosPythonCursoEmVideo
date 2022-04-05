print('Digite os 3 valores de retas e direi se é possível formar um triângulo:')
x = float(input('Primeiro valor:'))
y = float(input('Segundo valor:'))
z = float(input('Terceiro valor:'))

if abs(x - y) < z < x + y and abs(x - z) < y < x + z and abs(y - z) < x < y + z:
    print('Essas retas podem formar um triângulo! ')
    if x == y == z:
        print('O triângulo é equilátero!')
    elif x == y or x == z or y == z:
        print('O triângulo é isóceles')
    else:
        print('O triângulo é escaleno!')
else:
    print('Essas retas não podem formar um triângulo.')
