n = 0

while True:
    n = int(input('Deseja ver a tabuada de qual valor?'))
    if n < 0:
        print('Valor inválido')
        break
    for x in range(1,11):
        print(f'{n} x {x} = {n*x}')