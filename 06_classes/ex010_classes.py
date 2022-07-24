'''
Criar uma classe que representará uma aeronave militar com
o nome JatoMilitar1Lugar. O método construtor deverá receber
duas informações iniciais: o modelo e a base onde a aeronave
está; Crie um método chamado designar_piloto, que deverá
receber o nome do piloto como parâmetro

Criar um método rebasear_aeronave, que deverá receber de
parâmetro o nome da base para onde a aeronave deverá ser
enviada. Antes de registrar, é necessário validar se o piloto foi
designado para a aeronave, e somente se houver piloto, registrar
a informação de rebaseamento, a data e hora que a
movimentação foi realizada, deverá ser registrada também.
Sobrescreva o métod __str__ da classe, para imprimir o seguinte
conteúdo:
Jato: <NOME DA AERONAVE>
Base inicial: <NOME DA BASE DE ORIGEM>
Piloto: <NOME DO PILOTO DESIGNADO>
Histórico de transferências: <LISTAGEM DAS BASES PELAS QUAIS A
AERONAVE PASSOU MOSTRANDO A DATA / HORA E BASE>
'''


class JatoMilitar1Lugar:

    from datetime import datetime

    historico_de_bases = dict()

    def __init__(self, modelo: str, base_inicial: str) -> None:
        self.modelo = modelo
        self.base_inicial = base_inicial
        JatoMilitar1Lugar.historico_de_bases[self.base_inicial] = JatoMilitar1Lugar.datetime.now(
        ).strftime("%d/%m/%y %H:%M")

    def designar_piloto(self, nome_do_piloto: str) -> None:
        self.nome_do_piloto = nome_do_piloto

    def rebasear_aeronave(self, nova_base: str) -> None:
        if isinstance(self.nome_do_piloto, str):
            self.nova_base = nova_base
            JatoMilitar1Lugar.historico_de_bases[self.nova_base] = JatoMilitar1Lugar.datetime.now(
            ).strftime("%d/%m/%y %H:%M")
            print(f"Jato: {self.modelo}")
            print(f"Base Inicial: {self.base_inicial}")
            print(f"Piloto: {self.nome_do_piloto}")
            print(
                f"Histórico de transferências: {JatoMilitar1Lugar.historico_de_bases}")

        else:
            print("Um piloto precisa ser designado!")


jato_lia = JatoMilitar1Lugar("LiaDessault", "Area51")
jato_lia.designar_piloto("Lia")
jato_lia.rebasear_aeronave("Area52")
