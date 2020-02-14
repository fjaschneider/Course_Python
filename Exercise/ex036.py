casa = float(input('Qual o valor da casa: R$ '))
sal = float(input('Qual o seu Sálario? R$ '))
y = int(input('Em quantos anos você ira pagar? '))
pmax = sal * 0.3
if casa / (y * 12) >= pmax:
    print('Seu empréstimo foi NEGADO! Você poderia pagar no máximo R$ {:.2f} e sua prestação seria de R$ {:.2f}.'
          .format(pmax, casa / (y * 12)))
else:
    print('Seu empréstimo foi concedido, sua prestação será de R$ {:.2f}!'.format(casa / (y * 12)))
