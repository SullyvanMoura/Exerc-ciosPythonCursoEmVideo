print('Empréstimo bancário para comprar uma casa')

valor = float(input('Qual é o valor da casa?'))
salario = float(input('Qual o valor do seu salário?'))
anos = float(input('Em quantos anos você quer pagar a casa?'))

prest = valor/(12*anos)

if prest > 0.3*salario:
    print('Empréstimo negado!\nA prestação necessária de \033[7m{:.2f}\033[m é menor do que seu salário de {}.'.format(prest, salario))
else:
    print('O valor da prestação mensal será de \033[7m{:.2f}\033[m'.format(prest))