v = float(input('Qual a velocidade do carro? '))
if v <= 80:
    print('Parabéns, você está respeitando as leis de trânsito!')
else:
    print('Você foi multado em R$ {:.2f}, por estar dirrigindo a {} km/h. \n'
          '{} km/h a mais do permitido!'
          .format((v - 80)*7, v, v-80))
print('Dirrija com cuidado, respeite as leis de trânsito!')
