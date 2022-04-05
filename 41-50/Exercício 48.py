s = 0
cont = 0
for x in range(1,501,2):
    if x % 3 == 0:
        s = s + x
        cont= cont + 1
print('A soma de todos os números impares múltiplos de 3 até o número 500({} números) vale: {}'.format(cont,s))