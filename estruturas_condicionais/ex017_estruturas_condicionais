#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print('Digite uma data no formato xx/xx/xxxx')
dia = int(input('Digite um dia: '))
mes = int(input('Digite um mes: '))
ano = int(input('Digite um ano: '))
if dia > 0 and mes > 0 and mes <= 12:
    if mes >= 1 and mes <= 12:
        mesValido = True
    else:
        mesValido = False
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31 and dia >= 1:
            diaValido = True
        else:
            diaValido = False
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30 and dia >= 1:
            diaValido = True
        else:
            diaValido = False
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia <= 29 and dia >= 1:
                diaValido = True
        elif dia <= 28 and dia >= 1:
            diaValido = True
        else:
            diaValido = False
    if diaValido == True and mesValido == True:
        print('A data digitada: {}/{}/{} é válida'.format(dia,mes,ano))
    else:
        print('Data inválida!')
else:
        print('Data inválida!')
