print('{:=^50}'.format(' Schneider Store '))
p = float(input('Preço das compras: R$ '))
print('''Formas de pagamento:
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    print('O valor das compras ficou R$ {:.2f} com o desconto de 10%!'
          .format(p - (p*0.1)))
elif op == 2:
    print('O valor das compras ficou R$ {:.2f} com o desconto de 5%!'
          .format(p - (p * 0.05)))
elif op == 3:
    print('O valor das compras em duas vezes ficou de R$ {:.2f}!'
          .format(p / 2))
elif op == 4:
    par = int(input('Em quantas vezes você quer parcelar? '))
    print('O valor de sua parcela será de R$ {:.2f}!'.format((p + (p * 0.2))/par))
else:
    print('Opção inválida!')
