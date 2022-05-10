#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input('Digite um sexo (F ou M): ')
sexo = sexo.upper()
if sexo == 'F':
    print('O sexo digitado foi Feminino!')
elif sexo == 'M':
    print('O sexo digitado foi Masculino!')
else:
    print("Sexo inválido!")

#Aqui considerei que o programa deveria aceitar também letras digitadas em minúsculo considerando que o usuário as vezes não faz essa diferenciação