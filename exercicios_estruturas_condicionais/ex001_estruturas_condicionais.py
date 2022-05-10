#Faça um Programa que peça dois números e imprima o maior deles.
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

if numero_1 > numero_2:
    print(f"O maior número é {numero_1}")
elif numero_1 < numero_2:
    print(f"O maior número é {numero_2}")
else:
    print("Os números são iguais")

 # Aqui eu adicionei a parte dos números serem iguais pois percebi que seria uma possibilidade
