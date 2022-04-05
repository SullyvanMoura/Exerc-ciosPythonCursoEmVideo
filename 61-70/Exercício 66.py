n = 0

while True:
    n = int(input('Deseja ver a tabuada de qual valor?'))
    for x in range(1,11):
        print(f'{n} x {x} = {n*x}')