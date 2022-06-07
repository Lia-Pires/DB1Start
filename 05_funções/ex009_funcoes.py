'''Escreva um programa que execute uma função que
valide se o número informado é um número perfeito ou
não.
De acordo com a Wikipedia, um número perfeito é um número inteiro,
positivo que seja igual à soma de todos os seus divisores positivos
excluindo o próprio número. Equivalente a isto, um número perfeito é
a metade da soma de todos os seus divisores positivos, incluindo o
próprio número
Ex:
1 + 2 + 3 = 6
1 + 2 + 3 + 6 = 12 / 2 = 6
O próximo número perfeito seria 28.
1 + 2 + 4 + 7 + 14 = 28
'''

def perf_number(number):
    list = []
    for i in range(1, number):
            if number % i == 0:
                list.append(i)
    if sum(list) + number == number * 2:
        print(f"{number} is perfect")
    else:
        print(f"{number} isn't perfect") 


perf_number(6)
perf_number(28)
perf_number(7)