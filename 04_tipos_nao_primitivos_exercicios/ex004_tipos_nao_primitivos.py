'''Escreva um programa que conte o número de caracteres de uma string ( Exemplo: 'google.com'
Resultado Esperado: {'o': 3,'g': 2,'.': 1,'e': 1,'l': 1,'m': 1,'c': 1} )'''

from collections import Counter

string_ex = input("Digite uma frase: ")
contador_strings = dict(Counter(string_ex))

print(contador_strings)
