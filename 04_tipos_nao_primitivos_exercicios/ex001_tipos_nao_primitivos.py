# Escreva um programa que some todos os itens de uma lista.

lista = []
print("Vamos fazer uma lsita de números para ser somada!")
N = int(input("Quantos números vai colocar nessa lista? "))

while len(lista) < N:
    x = (input("Digite num número: "))
    if (x.isnumeric()):   #Aqui foi apenas para considerar a possibilidade do usuário digitar uma string.
        x = float(x)
        lista.append(x)
    else:
        print("Digite um número válido!")
soma = sum(lista)
print(f"A soma dos itens da lista digitada é: {soma}")
