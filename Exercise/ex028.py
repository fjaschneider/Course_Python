from random import randint
from time import sleep
pc = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jog = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('Processando...')
sleep(3)
if jog == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(pc, jog))
