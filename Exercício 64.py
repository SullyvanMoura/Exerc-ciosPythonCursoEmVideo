n = int(input('Tente advinhar o número inteiro que o computador pensou...(dica: esta entre 1 e 1000):'))
soma = n
count = 0

while n != 999:
    n = int(input('Errado! Mais uma chance:'))
    count += 1
    soma += n
print('Acertou! O número de vezes que tentou foi de {} e a soma dos números digitados(tirando o número flag) foi de {}!'.format(count + 1,soma - 999))