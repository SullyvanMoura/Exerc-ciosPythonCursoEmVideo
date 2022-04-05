lista = list()

resp = 'S'

while resp.upper() != 'N':
    x = int(input("Digite um valor: "))
    lista.append(x)
    resp = input("Deseja continuar? [S/N] ")

print(f"Você digitou {len(lista)} elementos")

lista.sort(reverse=True)

print(f"Os valores em ordem decrescente são {lista}")
cinco = 5 in lista
if cinco:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")