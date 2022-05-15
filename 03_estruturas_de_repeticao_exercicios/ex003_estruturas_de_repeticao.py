'''Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
negativos e o percentual de valores negativos e positivos.'''



continua = "S"
N = 0
soma = 0
negativos = 0
positivos = 0

while continua == "S":
    numero = float(input("Digite um número: "))
    N += 1
    soma = soma + numero
    if numero < 0:
        negativos += 1
    if numero > 0:
        positivos += 1
    continua = (input("Continuar? (S/N): ").upper())
    

media = soma / N
perc_negativos = negativos / N * 100
perc_positivos = positivos / N * 100

print(f"A média dos números digitados foi: {media}!")
print(f"A quantidade de números negativos digitados foi {negativos}!")
print(f"A quantidade de números positivos digitados foi {positivos}!")    
print(f"O percentual de números negativos foi de {perc_negativos}%!")
print(f"O percentual de números positivos foi de {perc_positivos}%!")   

