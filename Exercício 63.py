n = int(input('Quantos elementos você deseja ver da sequência de Fibonacci?'))
t1 = 0
t2 = 1
t3 = t1 + t2

count = 0
if n == 1:
    print('0 -> ',end='')
elif n == 2:
    print('0 -> 1 -> ',end='')
else:
    print('0 -> 1 -> ', end='')
    while count != n-2:
        t3 = t1 + t2
        print(t3,end=' -> ')
        t1 = t2
        t2 = t3
        count += 1
print('FIM')
input('Pressione qualquer tecla para sair')