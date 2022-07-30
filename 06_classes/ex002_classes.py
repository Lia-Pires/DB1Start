'''
Escreva uma classe em Python para converter um
número romano em um número inteiro

'''

class Romano:

    equivalente = {"I":1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    def __init__(self, romano:str):
        self.romano = romano

    