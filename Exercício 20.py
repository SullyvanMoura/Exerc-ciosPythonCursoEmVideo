a = input('Qual o nome do primeiro aluno?')
b = input('Qual o nome do segundo aluno?')
c = input('Qual o nome do terceiro aluno?')
d = input('Qual o nome do quarto aluno?')
list = [a,b,c,d]
import random
random.shuffle(list)
print('A ordem de apresentação do trabalho será a seguinte:')
print(list)
