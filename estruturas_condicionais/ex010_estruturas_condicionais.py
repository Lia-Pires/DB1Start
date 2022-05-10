'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
 
salarioAtual = float(input('Digite o salário atual: '))

if salarioAtual <= 280.00:
    salarioReajustado = salarioAtual * 1.2
    percentual = 20
elif salarioAtual > 280.00 and salarioAtual <= 700.00:
    salarioReajustado = salarioAtual * 1.15
    percentual = 15
elif salarioAtual > 700.00 and salarioAtual <= 1500.00:
    salarioReajustado = salarioAtual * 1.10
    percentual = 10
elif salarioAtual > 1500.00:
    salarioReajustado = salarioAtual * 1.05
    percentual = 5
 
valorAumento = salarioReajustado - salarioAtual
 
print(f'Salário inicial: R${salarioAtual:.2f}.')
print(f'O percentual de aumento foi: {percentual}%.')
print(f'O valor do aumento foi: R${valorAumento:.2f}.')
print(f'O salário com reajuste é: R${salarioReajustado:.2f}')