'''
Escreva uma classe em Python para converter um
número inteiro em um numeral romano.

'''
class Numero:
    equivalente = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

    def __init__(self, inteiro:int) -> None:        
        self.inteiro = inteiro

    def romano(self):
        valores = [keys for keys in Numero.equivalente.keys()]
        resultado= []

        a = self.inteiro
      
        while a != 0:
            for x in range(-1,-1-len(valores), -1):
                while a >= valores[x]:
                    if a >= valores[x]:
                        resultado.append(Numero.equivalente[valores[x]])
                        a = a - valores[x]

        
        valor_final = "".join(resultado)
        
        return valor_final    


# numero = Numero(10)
# numero = Numero(11)
# numero = Numero(50)
# numero = Numero(500)
# numero = Numero(434)
numero = Numero(700)

print(numero.romano())
    