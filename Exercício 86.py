matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input(f"Digite o valor na posição [{i}][{j}]: ")))

for i in range(0,3):
    for j in range(0,3):
        print(matriz[i][j], end=' ')
    print()