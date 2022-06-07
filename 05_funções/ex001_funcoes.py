''' Escreva um programa que execute uma função que
encontre o maior número de uma lista passada por
parâmetro.
'''


def higher_number(list):
    print(f"The higher number of the given list is: {max(list)}")


higher_number([1, 7, 10, 11, 45])
higher_number([8, 5000, 15, 150, 1020])
higher_number([0, -2, 3010,-250, 360])
higher_number([7, 1, 2, 3, 4, 5, 6])