'''Escreva um programa que execute uma função que
calcule o fatorial de um número passado por parâmetro.'''


def factorial_number(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i

    print(f"The factorial of {number} is: {factorial}")


factorial_number(10)
factorial_number(7)
factorial_number(8)
factorial_number(50)