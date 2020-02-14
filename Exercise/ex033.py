a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verrificar o menor valor.
less = a
if b < a and b < c:
    less = b
if b < a and c < d:
    less = c
# Verrificar o maior valor.
high = a
if b > a and b > c:
    high = b
if c > a and c > b:
    high = c
print('O menor valor digitado foi {}!'.format(less))
print('O maior valor digitado foi {}!'.format(high))
