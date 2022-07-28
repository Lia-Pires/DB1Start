'''
Criar uma classe Triangulo, que receba no seu
construtor 3 medidas de ângulos. Criar um método
check_angulo que valide as informações dos 3 ângulos
informados na criação da classe.

Instanciar a classe Triangulo e imprimir os lados
informados e imprimir se o triângulo é um triângulo ou não.
O método check_angulo deverá retornar True se a
soma dos valores for igual a 180 e False em qualquer outra
possibilidade;

'''


class Triangulo:

    def __init__(self, anga, angb, angc):
        self.a = anga
        self.b = angb
        self.c = angc


    def CheckTriangulo(self):
        if (abs(self.b-self.c) < self.a and self.a < (self.b+self.c)) or (abs(self.a-self.c) < self.b and self.b < (self.a+self.c)) or (abs(self.a-self.b) < self.c and self.c < (self.a+self.b)):
            print("O triângulo é real!")
        
        else:
            print("O triângulo não existe.")
            

triangulo_teste = Triangulo(5, 4, 3)

triangulo_teste.CheckTriangulo();

