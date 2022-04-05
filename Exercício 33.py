a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))

menor = a
if b<a and b<c:
    menor = b
elif c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior =  b
elif c>b and c>a:
    maior = c

print('O maior dos números é {}\nO menor dos números é {}'.format(maior, menor))