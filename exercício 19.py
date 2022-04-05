a = input('Qual o nome do primeiro aluno?')
b = input('Qual o nome do segundo aluno?')
c = input('Qual o nome do terceiro aluno?')
d = input('Qual o nome do quarto aluno?')
list = [a,b,c,d]
import random
n = random.choice(list)
print('O aluno escolhido foi {}!'.format(n))
