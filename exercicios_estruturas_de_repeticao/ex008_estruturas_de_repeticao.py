'''Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
P.A. contendo 10 valores.'''

A = int(input("Digite o valor Inicial: "))
R = int(input("Digite a razão: "))
decimo = A + (10 - 1) * R

for i in range(A, decimo + R, R):
    print(f'{i}')