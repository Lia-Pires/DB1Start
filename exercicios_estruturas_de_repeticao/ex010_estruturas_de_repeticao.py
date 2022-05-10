'''Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de
A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120'''

A = int(input("Digite um valor para obter seu fatorial: "))
contador = A
resultado = 1

while contador > 1:
    resultado = resultado * (contador)
    contador -= 1
print(f"{A}! é = {resultado}")   