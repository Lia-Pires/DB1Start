'''
Escreva uma classe em Python que receba como
arqumentos um id, um nome e a classe de um estudante,
sendo que o nome e a classe não são obrigatórios no
momento da instanciação da classe. Crie um método
que imprima o id do aluno, e se houver nome, imprima o
nome, e se houver classe, imprima a classe também.

'''

class Aluno:

    def __init__(self, id: int, nome = 0, classe = 0):
        self.id = id
        self.nome = nome
        self.classe = classe

    def dados_do_aluno(self) -> str:
        if isinstance(self.nome, str) and isinstance(self.classe, str):
            return self.id, self.nome, self.classe
        elif isinstance(self.nome, str):
            return self.id, self.nome
        elif isinstance(self.classe, str):
            return self.id, self.classe
        else: 
            return self.id

lia = Aluno(78900, "Lia", "Primeiro_ano")
# lia = Aluno(78900, "Lia")
# lia = Aluno(78900, "Primeiro_ano")
# lia = Aluno(78900)

print(lia.dados_do_aluno())


    