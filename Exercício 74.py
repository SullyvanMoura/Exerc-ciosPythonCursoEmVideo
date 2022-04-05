from random import randint

números = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print('Os valores sorteados foram: ',end='')
for n in números:
    print(n,end=' ')

x = len(números) - 1

print('\nO maior número é {}'.format(sorted(números)[x]))
print('O menor número é {}'.format(sorted(números)[0]))