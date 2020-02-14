import math
ang = float(input('Informe o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('Para o ângulo {:.2f} o valor de seno é {:.2f}, do cosseno é {:.2f} e a sua tangente é {:.2f}'
      .format(ang, sen, cos, tg))
