#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')
letra = letra.lower()
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Você digitou uma vogal!')
elif letra.isalpha():
    print('Você digitou uma consoante!')
else:
    print('Não é uma letra!')
 # Aqui também considerei que o usuário pode digitar uma letra maiúscula ou minúscula e o caso de não ser digitado uma letra
