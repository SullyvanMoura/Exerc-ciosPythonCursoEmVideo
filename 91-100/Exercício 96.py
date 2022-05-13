def area(x,y):
    print(f'A área do terreno {x} x {y} é {x*y}m²')

print('Digite as dimensões da área do terreno em m²: ')
altura = float(input('Altura: '))
largura = float(input('Largura: '))

area(altura, largura)