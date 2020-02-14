from datetime import date
today = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
y = today - nasc
print('Você nasceu em {} e tem {} anos!'.format(nasc, today - nasc))
if today - nasc > 18:
    print('Você deve ter se alistado a {} anos!'
          .format(today - (nasc + 18)))
elif today - nasc < 18:
    print('Você deve se alistar da qui a {} anos!'
          .format(18 - (today - nasc)))
elif today - nasc == 18:
    print('Você deve se alistar imediatamente!')
