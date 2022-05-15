# Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500. 
soma = 0
for x in range(501):
    if x % 2 != 0 and x % 3 == 0:
        soma += x

print(soma)



