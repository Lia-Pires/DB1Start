'''Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
números lidos. O número que encerrará a leitura será zero.'''


quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma = 0
N = 0

numero = float(input("Digite um número positivo: "))
while numero != 0:
    soma += numero
    N += 1
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    if numero % 2 != 0:
        quantidade_impares += 1
    numero = float(input("Digite um número positivo: "))


print(f"Foram digitados {quantidade_pares} números pares e {quantidade_impares} números ímpares.")
print(f"A média dos valores pares digitados é: {soma_pares/quantidade_pares} ")
print(f"A média de todos os números digitados é {soma / N}!")




