''' Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
mostrar :
a. A menor altura do grupo;
b. A maior altura do grupo;'''

menor_altura = 500.0
maior_altura = 1.0
altura = 1.0

for i in range(15):
    altura = float(input("Digite a altura de uma pessoa: "))
    if altura < menor_altura:
        menor_altura = altura
    if altura > maior_altura:
        maior_altura = altura
i += 1

print(f"A maior altura é {maior_altura}m!")
print(f"A menor altura é {menor_altura}m!") 

