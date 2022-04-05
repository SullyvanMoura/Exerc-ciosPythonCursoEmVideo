tupla = ("Lápis" , 1.75, "Borracha", 2.0, "Caderno" , 15.90, "Estojo", 25.0,
         "Trasferidor", 4.20, "Compasso", 9.99, "Mochila", 99.90, "Kit Canetas", 22.30, "Livro", 35.60)

print("-"*40)
print("{:^40}".format("Listagem de Preços"))
print("-"*40)

for coisa in tupla:
    if isinstance(coisa, str):
        print(coisa, end= '')
        print('.'*(31 - len(coisa)),end= "R$")

    elif isinstance(coisa, float):
        print("{:>7.2f}".format(coisa))

