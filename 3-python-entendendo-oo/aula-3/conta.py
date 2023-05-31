class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto ... {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'O titular {self.titular} possui {self.saldo} de saldo')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
