pri = int(input('Qual é o primeiro termo da Progressão Aritmética?'))
raz = int(input('Qual é a razão da progressão aritmética?'))

print('Os 10 primeiros termos dessa PA são:')

for x in range(pri,pri + 10*raz ,raz):
     print(x,end= ' -> ')