name = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é {}.'.format(name.upper()))
print('Seu nome em letras minúsculas é {}.'.format(name.lower()))
print('Seu nome possui {} letras.'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(name.find(' ')))
sep = name.split()
print('Seu primeiro nome {} tem {} letras.'.format(sep[0], len(sep[0])))