'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

diaDaSemana = int(input('Digite um número de 1 à 7: '))
if diaDaSemana == 1:
    print('Domingo')
elif diaDaSemana == 2:
    print('Segunda-Feira')
elif diaDaSemana == 3:
    print('Terça-feira')
elif diaDaSemana == 4:
    print('Quarta-feira')
elif diaDaSemana == 5:
    print('Quinta-feira')
elif diaDaSemana == 6:
    print('Sexta-feira')
elif diaDaSemana == 7:
    print('Sábado')
else:
    print('Dia da semana inválido!')
