lista = list()

resp = 'S'

while resp.upper() != 'N':
    x = int(input("Digite um valor: "))
    lista.append(x)
    resp = input("Deseja continuar? [S/N] ")

par = []
impar = []

for value in lista:
    if value%2 == 0:
        par.append(value)
    else:
        impar.append(value)

print(f"Lista original: {lista}")
print(f"Valores pares da lista {par}")
print(f"Valores ímpares da lista {impar}")