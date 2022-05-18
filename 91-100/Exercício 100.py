from random import randint
from time import sleep

lista = list()

def sorteia(lst):
    print('Sorteando valores: ')
    for i in range(5):
        sleep(0.5)
        v = randint(0,20)
        print(v,end=' ',flush=True)
        lst.append(v)
    print()

def soma_par(lst):
    total = 0
    for v in lista:
        if v % 2 == 0:
            total+=v
    print(f'A soma dos valores pares da lista é {total}')

sorteia(lista)
soma_par(lista)