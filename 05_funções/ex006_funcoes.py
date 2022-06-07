'''Escreva um programa que execute uma função que
conte o número de letras maiúsculas e minúsculas de
um texto e que ao final, chame outra função para
imprimir o resultado'''

import re

def upper_and_lower(string):
    upper = re.findall(r"[A-Z]", string)
    lower = re.findall(r"[a-z]", string)
    lenght_upper = len(upper)
    lenght_lower = len(lower)

   
    def print_characteres():
        print(f"The amount of upper case characteres on the given string is {lenght_upper}")
        print(f"The amount of lower case characteres on the given string is {lenght_lower}")
    
    return print_characteres()


upper_and_lower("PyThOn is ReaLLy FuN")

  