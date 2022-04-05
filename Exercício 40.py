x = float(input('Digite sua primeira nota:'))
y = float(input('Digite sua segunda nota:'))

m = (x + y)/2

if x > 10 or y > 10:
    print('Nota inválida!')

if m < 5 and x <= 10 and y <= 10:
    print('Sua média foi {:.1f}.\n\033[31mReprovado\033[m!'.format(m))
elif 5 <= m < 7 and x <= 10 and y <= 10:
    print('Sua média foi {:.1f}.\n\033[33mRecuperação!\033[m'.format(m))
elif 7 <= m <= 10 and x <= 10 and y <= 10:
    print('Sua média foi {}.\n\033[32mAprovado!\033[m'.format(m))

input('Pressione Enter para sair')