m = float(input('Qual o seu peso (kg)? '))
h = float(input('Qual sua altura (m)?'))
imc = m / (h ** 2)
print('O IMC dessa pessoa é de {:.2f}!'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')