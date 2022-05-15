#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
raioDoCirculo = float(input("Digite o raio do círculo: "))
areaDoCirculo = math.pi * (raioDoCirculo ** 2)
print("A área do círculo é de {:.2f} um²".format(areaDoCirculo))
# Considerando "um" como "unidade de medida"
