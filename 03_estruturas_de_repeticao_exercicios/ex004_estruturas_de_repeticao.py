'''Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
terminar quando for lido um número negativo. '''


continua = "S"
intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0

while continua == "S":
    numero = float(input("Digite um número: "))
    if numero >= 0 and numero <= 25:
        intervalo_1 += 1
    if numero >= 26 and numero <= 50:
        intervalo_2 += 1
    if numero >= 51 and numero <= 75:
        intervalo_3 += 1
    if numero >= 76 and numero <= 100:
        intervalo_4 += 1
    continua = input("Continuar (S/N): ").upper()

print(f"Foram digitados {intervalo_1} numeros entre 0 e 25!")
print(f"Foram digitados {intervalo_2} numeros entre 26 e 50!")
print(f"Foram digitados {intervalo_3} numeros entre 51 e 75!")
print(f"Foram digitados {intervalo_4} numeros entre 76 e 100!")
