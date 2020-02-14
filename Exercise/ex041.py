from datetime import date
y = int(input('Qual o ano de nascimento do atleta: '))
id = (date.today().year - y)
print('O atleta tem {} anos e é classificado como:'.format(id))
if id <= 9:
    print('MIRIM')
elif id <= 14:
    print('INFANTIL')
elif id <= 19:
    print('JÚNIOR')
elif id <= 25:
    print('SÊNIOR')
else:
    print('MASTER')