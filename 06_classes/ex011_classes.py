'''
Criar uma classe que representará outro tipo de aeronave
militar, com o nome JatoMilitar2Lugares. O método construtor
deverá receber duas informações: o modelo, e a base onde a
aeronave está; Cria um método chamado designar_piloto que
everá contar o nome do piloto. Por regra, o primeiro piloto
será considerado o piloto principal e o segundo, o seu copiloto. Depois de informados os dois nomes, não poderá ser
inserido mais nenhum nome.


Criar um método rebasear_aeronave, que receberá como
parâmetro o nome da base para onde a aeronave deverá ser
enviada. Antes de registrar, é necessário validar se dois pilotos
foram designados para a aeronave, e somente se ambos tiverem
sido designados, registrar o rebaseamento, com a data e hora da
movimentação.

Sobrescreva o métod __str__ da classe, para imprimir o seguinte
conteúdo:
Jato: <NOME DA AERONAVE>
Base inicial: <NOME DA BASE DE ORIGEM>
Piloto: <NOME DOS PILOTOS DESIGNADOS>
Histórico de transferências: <LISTAGEM DAS BASES PELAS QUAIS A
AERONAVE PASSOU MOSTRANDO A DATA / HORA E BASE>

'''


class JatoMilitar2Lugares:

    from datetime import datetime

    historico_de_bases = dict()

    def __init__(self, modelo: str, base_inicial: str) -> None:
        self.modelo = modelo
        self.base_inicial = base_inicial
        JatoMilitar2Lugares.historico_de_bases[self.base_inicial] = JatoMilitar2Lugares.datetime.now().strftime("%d/%m/%y %H:%M")

    def designar_piloto(self, nome_do_piloto: str, nome_do_copiloto) -> None:
        self.nome_do_piloto = nome_do_piloto
        self.nome_do_copiloto = nome_do_copiloto

    def rebasear_aeronave(self, nova_base: str) -> None:
        if isinstance(self.nome_do_piloto, str) and isinstance(self.nome_do_copiloto, str):
            self.nova_base = nova_base
            JatoMilitar2Lugares.historico_de_bases[self.nova_base] = JatoMilitar2Lugares.datetime.now().strftime("%d/%m/%y %H:%M")
            print(f"Jato: {self.modelo}")
            print(f"Base Inicial: {self.base_inicial}")
            print(f"Piloto: {self.nome_do_piloto}")
            print(f"Copiloto: {self.nome_do_copiloto}")
            print(f"Histórico de transferências: {JatoMilitar2Lugares.historico_de_bases}")

        else:
            print("Um piloto precisa ser designado!")


jato_lia = JatoMilitar2Lugares("LiaDessault", "Area51")
jato_lia.designar_piloto("Lia", "Pires")
jato_lia.rebasear_aeronave("Area52")
