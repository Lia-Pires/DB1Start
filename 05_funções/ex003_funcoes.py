'''Escreva um programa que execute uma função que
multiplique todos os números de uma lista passada por
parâmetro.'''

from math import prod

def multiply_list(list):
    prod_list = prod(list)
    print(f"The product of a multiplication of all the given list numbers is: {prod_list}")

multiply_list([5, 2, 1])
multiply_list([1, 4, 10, 7, 28])
multiply_list([-1, 2, 30, 56])