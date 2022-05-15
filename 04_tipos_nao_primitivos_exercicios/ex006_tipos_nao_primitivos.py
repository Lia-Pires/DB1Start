'''Escreva um programa que ordene em ordem crescente uma lista de tuplas informadas, pelo último item da tupla (Exemplo de lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Resultado esperado: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] )'''

lista = []
N = int(input("Quantas tuples você vai digitar? "))

while len(lista) < N:
    x = tuple((input("Digite uma tuple (Apenas os números, sem espaços ou virgulas: ")))
    lista.append(x)

for i in range(len(lista)):
    lista[i] = list(lista[i])

for i in range(len(lista)):
    for j in range(len(lista[i])):
        lista[i][j] = int(lista[i][j])

for i in range(len(lista)):
    lista[i] = tuple(lista[i])

lista.sort(key=lambda x: x[1], reverse=False)
print(lista)