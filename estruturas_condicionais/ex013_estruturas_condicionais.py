'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo: Média de Aproveitamento Conceito Entre 9.0 e 10.0 A Entre 7.5 e 9.0 B Entre 6.0 e 7.5 C Entre 4.0 e 6.0 D Entre 4.0 e zero
E O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

nota_1 = float(input('Digite a primeira nota parcial: '))
nota_2 = float(input('Digite a segunda nota parcial: '))
media = (nota_1 + nota_2) / 2

if media <= 10.0 and media >= 0:
    if media <= 10.0 and media > 9.0:
        conceito = 'A'
        situação = 'APROVADO!'
    elif media <= 9.0 and media > 7.5:
        conceito = 'B'
        situação = 'APROVADO!'
    elif media <= 7.5 and media > 6.0:
        conceito = 'C'
        situação = 'APROVADO!'
    elif media <= 6.0 and media > 4.0:
        conceito = 'D'
        situação = 'REPROVADO!'
    elif media <= 4.0 and media > 0.0:
        conceito = 'E'
        situação = 'REPROVADO!'
    print(f'Média do aluno: {media:.1f}')
    print(f'Conceito do aluno: {conceito}')
    print(f'Situação do aluno: {situação}')

else:
    print('Nota inválida!')

