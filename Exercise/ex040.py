n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
nf = (n1 + n2) / 2
if nf > 7:
    print('Sua nota foi {:.2f}, PARABÉNS, você foi aprovado!'.format(nf))
elif nf < 5:
    print('Sua nota é {:.2f} você está reprovado!'.format(nf))
else:
    print('Sua nota é {:.2f} você está em recuperação!'.format(nf))
