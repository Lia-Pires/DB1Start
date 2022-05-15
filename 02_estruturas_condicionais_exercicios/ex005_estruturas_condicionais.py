'''Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada pelo aluno e apresentar:"
 A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez."'''

nota_1 = float(input('Digite a primeira nota parcial: '))
nota_2 = float(input('Digite a segunda nota parcial: '))
media = (nota_1 + nota_2) / 2

if media >= 7.0 and media < 10.0:
    print('Aluno aprovado!')
elif media < 7.0:
    print('Aluno reprovado!')
elif media == 10.0:
    print('Aluno aprovado com distinção!')