km = float(input('Quantos Km foram percorridos? '))
dias = float(input('Quantos dias foram alugados? '))
pkm = km * 0.15
pdias = dias * 60
print('O carro percorreu uma distância de {:.1f} Km e foi alugado por {:.0f} dias. \n'
      'Sendo assim o preço do aluguel do carro ficou em R$ {:.2f}'
      .format(km, dias, pkm + pdias))
