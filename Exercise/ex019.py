import random
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do outro aluno: ')
a3 = input('Digite o nome do outro aluno: ')
a4 = input('Digite o nome do outo aluno:')
lista = [a1, a2, a3, a4]
esc = random.choice(lista)
print('O aluno sorteado foi {}!'.format(esc))
