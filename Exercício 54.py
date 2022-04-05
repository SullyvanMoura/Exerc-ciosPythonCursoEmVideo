from datetime import date

ano = date.today().year

cont = 0
for x in range(0,7):
    a = int(input('Em qual ano você nasceu?'))
    if ano - a <= 18:
        cont += 1
print('Dos 7 participantes, {} possivelmente são menores de idade!'.format(cont))