'''Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres
sejam iguais. (Exemplo de lista: ['abc','xyz','aba','1221'] Resultado esperado: 2 )'''


lista_matriz = []
print("Vamos fazer uma lista de strings!")
N = int(input("\nQuantos itens vai colocar nessa lista? "))

while len(lista_matriz) < N:
    x = (input("Digite algo: "))
    lista_matriz.append(x)

lista_filha = []

for string in lista_matriz:
    lista_filha.append(list(string))

contador = 0

for i in range(len(lista_filha)):
        if lista_filha[i][0] == lista_filha [i][-1] and len(lista_filha[i]) > 2:
            contador += 1

print(f"Na sua lista digitada {lista_matriz}:\nA quantidade de itens que são maiores que 2 caracteres e tem o primeiro e o último caracter iguais são {contador}")
