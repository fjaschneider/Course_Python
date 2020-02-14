salario = float(input('Escreva o salário do funcionário: R$ '))
if salario > 1250:
    print('O salário de R$ {:.2f} com o ajuste ficou R$ {:.2f}'
          .format(salario, (salario * 0.1) + salario))
else:
    print('O salário de R$ {:.2f} com o ajuste ficou R$ {:.2f}'
          .format(salario, (salario * 0.15) + salario))
