'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.#
Desconto do IR:
Salário Bruto até 900 (inclusive) – isento
Salário Bruto até 1500 (inclusive) – desconto de 5%
Salário Bruto até 2500 (inclusive) – desconto de 10%
Salário Bruto acima de 2500 – desconto de 20% Imprima na tela as informações
'''
 
 
horas = float(input('Digite a quantidade de horas trabalhadas: '))
valorHora = float(input('Digite o valor da hora trabalhada: '))
salarioBruto = horas * valorHora
Fgts = salarioBruto * 0.11
descSindicato = salarioBruto * 0.03
 
if salarioBruto <= 900.00:
    salarioLiquido = salarioBruto - descSindicato
    percentualIR = 0
    descIR = 0.00
elif salarioBruto > 900.00 and salarioBruto <= 1500.00:
    descIR = salarioBruto * 0.05
    salarioLiquido = salarioBruto - descSindicato - descIR
    percentualIR = 5
elif salarioBruto > 1500.00 and salarioBruto <= 2500.00:
    descIR = salarioBruto * 0.10
    salarioLiquido = salarioBruto - descSindicato - descIR
    percentualIR = 10
elif salarioBruto > 2500.00:
    descIR = salarioBruto * 0.20
    salarioLiquido = salarioBruto - descSindicato - descIR
    percentualIR = 20
 
print(f'O seu salário bruto é de: R${salarioBruto:.2f}.')
print(f'O valor do seu FGTS (11%) nesse mês é de: R${Fgts:.2f}.')
print(f'O desconto do sindicato (3%) foi de: R${descSindicato:.2f}.')
print(f'O desconto do imposto de renda ({percentualIR}%) foi de: R${descIR:.2f}.')
print(f'O seu salário líquido é de: R${salarioLiquido:.2f}')

