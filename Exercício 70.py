print('-_'*10)
print('MERCADINHO BIG-BOM!')
print('-_'*10)

total = 0
mais100 = 0
menor = 0
count = 0
barato = ' '

while True:
    nome = str(input('Nome do Produto:'))
    preço = float(input('Preço do Produto: R$'))
    count += 1
    total += preço
    if count == 1 or preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        mais100 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja adicionar mais produtos? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}\nO número de produtos custando acima de R$1000.00 foi de {mais100}\nO produto mais barato foi {barato}, custando R${menor:.2f} ')