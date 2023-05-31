# Desafio aula 03

# comandos para rodar no Python Console:
# from datas import Data
# data_obj = Data(31,5,2023)
# print(data_obj.formata_data())

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)

    def formata_data(self):
        return f'{self.dia:02d}/{self.mes:02d}/{self.ano:4d}'
