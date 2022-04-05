matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input(f"Digite o valor na posição [{i}][{j}]: ")))

totalPares = 0
totalTerceira = 0

for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j] % 2 == 0:
            totalPares += matriz[i][j]
        if j == 2:
            totalTerceira += matriz[i][j]
        if i == 1:
            if j == 0:
                maior = matriz[i][j]
            else:
                if matriz[i][j] > maior:
                    maior = matriz[i][j]


for i in range(0,3):
    for j in range(0,3):
        print(matriz[i][j], end=' ')
    print()

print(f"A soma dos valores pares é igual a {totalPares}")
print(f"A soma dos valores da terceira coluna é igual a {totalTerceira}")
print(f"O maior valor da segunda linha é {maior}")