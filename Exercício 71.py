print('-'*25)
print('BANCO DO BANCO DO BANCO')
print('-'*25)

n = int(input('Qual valor você deseja sacar? R$'))
total = n

céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd +=1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} de cédulas de R${céd}')
        if céd == 50:
            céd = 20
            totcéd = 0
        elif céd == 20:
            céd = 10
            totcéd = 0
        elif céd == 10:
            céd = 1
            totcéd = 0
        if total == 0:
            break
print('Obrigado! Volte Sempre!')