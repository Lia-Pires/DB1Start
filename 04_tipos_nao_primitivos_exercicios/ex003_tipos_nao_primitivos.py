# Escreva um programa que retorne o maior e o menor número de uma lista.
lista = []
print("Vamos fazer uma lsita de números!")
N = int(input("Quantos números vai colocar nessa lista? "))

while len(lista) < N:
    x = (input("Digite num número: "))
    if (x.isnumeric()):   #Aqui foi apenas para considerar a possibilidade do usuário digitar uma string.
        x = float(x)
        lista.append(x)
    else:
        print("Digite um número válido!")
maior_valor = (max(lista))
print(f"O maior valor da lista digitada é: {maior_valor}!")