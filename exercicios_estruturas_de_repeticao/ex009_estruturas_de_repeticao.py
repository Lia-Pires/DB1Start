'''Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
P.G. contendo 10 valores.'''

A = int(input("Digite o valor Inicial: "))
R = int(input("Digite a razão: "))
contador = 0
while contador < 10:
    A = A * R
    print(f"{A}")
    contador += 1
