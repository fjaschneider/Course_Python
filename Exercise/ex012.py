p = float(input('Qual o valor do produto? R$ '))
print('O valor do produto é R$ {:.2f}, com 5% de desconto vai para R$ {:.2f}!'
      .format(p, p-p*0.05))
