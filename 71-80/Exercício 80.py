lista = list()

for i in range(0,5):
    x = int(input("Digite um valor: "))
    if i == 0 or x > lista[-1]:
        lista.append(x)
        print("Adicionado à ultima posição")
    else:
        j = 0
        while j < len(lista):
            if  x <= lista[j]:
                lista.insert(j,x)
                print(f'Adicionado à posição {j}')
                break
            j +=1

print(lista)