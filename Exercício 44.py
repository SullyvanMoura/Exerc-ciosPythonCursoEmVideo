print('{:-^60}'.format('Preço do produto considerando condição de pagamento'))

preç = float(input('Qual o preço do produto que deseja comprar?'))

print('Considerando os métodos de pagamento abaixo:\n'
      '1. À vista no dinheiro/cheque(10% de desconto)\n'
      '2. À vista no cartão(5% de desconto)\n'
      '3. Em até 2x no cartão\n'
      '4. 3x ou mais no cartão(20% de juros no valor total do produto)')

x = int(input('Qual a opção desejada?'))

if x == 1:
    valor = 0.9 * preç
    print('O valor da compra será de R${:.2f}'.format(valor))
elif x == 2:
    valor = 0.95 * preç
    print('O valor da compra será de R${:.2f}'.format(valor))
elif x == 3:
    valor = preç
    print('O valor da compra será de R${:.2f}'.format(valor))
elif x == 4:
    valor = 1.2 * preç
    print('O valor da compra será de R${:.2f}'.format(valor))
else:
    print('Opção inválida')

input('Pressione ENTER para sair')
