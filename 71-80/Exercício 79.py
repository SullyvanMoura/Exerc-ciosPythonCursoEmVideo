lista = list()

resp = 'S'

while resp.upper() not in 'N':
    x = int(input("Digite um valor: "))
    if x not in lista:
        lista.append(x)

    resp = str(input('Deseja continuar? [S/N] '))

print(lista)