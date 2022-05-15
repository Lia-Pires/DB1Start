# Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

pares = []
impares = []

for i in range(100,201):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Os números ímpares entre 100 e 200 são: {impares}")
print(f"Os números pares entre 100 e 200 são: {pares}")