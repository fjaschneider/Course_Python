l = float(input('Qual a largura da parede (m)? '))
a = float(input('Qual a altura da parede (m)? '))
area = l * a
tinta = area / 2
print('A área da parede é {}x{} m, correspondendo a {} m². \n'
      'Você precisa de {} litros de tinta para cobrir a parede!'
      .format(l, a, area, tinta))
