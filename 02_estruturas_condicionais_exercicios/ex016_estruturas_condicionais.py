'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

anoDigitado = int(input('Digite um ano: '))
if (anoDigitado % 4 == 0 and anoDigitado % 100 != 0) or (anoDigitado % 400 == 0):
    print('O ano digitado é bissexto')
else:
    print('O ano digitado não é bissexto')

