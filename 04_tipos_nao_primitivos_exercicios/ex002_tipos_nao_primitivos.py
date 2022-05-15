# Escreva um programa que multiplique todos os itens de uma lista.

lista = []
print("Vamos fazer uma lista de números para ter seus itens multiplicados!")
N = int(input("\nQuantos números vai colocar nessa lista? "))

while len(lista) < N:
    x = (input("Digite num número: "))
    if (x.isnumeric()):   #Aqui foi apenas para considerar a possibilidade do usuário digitar uma string.
        x = float(x)
        lista.append(x)
    else:
        print("Digite um número válido!")

print(f"\nA lista digitada foi: {lista}")

m = (input("\nPor qual valor você quer que cada item da sua lsita seja multiplicado? "))
if (m.isnumeric()):
    m = float(m)

#Aqui eu fiz duas possibilidades pois não estava bem explicado se era pra multiplicar cada item por um valor ou fazero valor aparecer número m de vezes
#Fazendo os itens aparecerem mais vezes:
lista_2 = lista * 2
print(f"\nA lista com seus itens aparecendo {m} vezes é: {lista_2}")

#Fazendo cada item da lista ser múltiplicado por m
lista_3 = []
for i in lista:
    lista_3.append(i * m)
print(f"A lista com seus valor multiplicados por {m} é: {lista_3}")



