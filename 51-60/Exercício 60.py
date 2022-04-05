n = int(input('Digite um número e darei seu fatorial:'))
resultado = 1
while n > 0:
    resultado = resultado*(n)
    n = n - 1
print(resultado)