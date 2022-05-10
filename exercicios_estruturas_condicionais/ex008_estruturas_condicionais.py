# Faça um programa que leia três números e mostre-os em ordem decrescente.

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))
 

if numero_1 == numero_2 and numero_2 == numero_3:
    print('Os números são iguais!')
else:
    maior = numero_1
    if numero_2 > numero_1 and numero_2 > numero_3:
            maior = numero_2
    elif numero_3 > numero_1 and numero_3 > numero_2:
            maior = numero_3
         
    if numero_2 < numero_3 and numero_2 < numero_1:
            menor = numero_2
    elif numero_3 < numero_2 and numero_3 < numero_1:
            menor = numero_3
    elif numero_1 < numero_2 and numero_1 < numero_3:
            menor = numero_1      
    if numero_2 < maior and numero_2 > menor:
            medio = numero_2
    elif numero_3 < maior and numero_3 > menor:
            medio = numero_3
    elif numero_1 < maior and numero_1 > menor:
            medio = numero_1
 


print(f'Os números digitados em ordem decrescente são: {maior}, {medio}, {menor}')
 
