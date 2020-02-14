from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jog = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-x-' * 10)
print('O computador jogou {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[jog]))
print('-x-' * 10)
if pc == 0:
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('VOCÊ VENCEU!')
    elif jog == 2:
        print('VOCÊ PERDEU!')
    else:
        print('Jogada inválida!')
elif pc == 1:
    if jog == 0:
        print('VOCÊ PERDEU!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('VOCE GANHOU!')
    else:
        print('Jogada inválida!')
elif pc == 2:
    if jog == 0:
        print('VOCÊ GANHOU!')
    elif jog == 1:
        print('VOCÊ PERDEU!')
    elif jog == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')