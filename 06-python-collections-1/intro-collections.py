from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaIvenstimento(Conta):
    pass


@total_ordering
class ContaSalario():
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

print('')

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)

print('')

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
print(conta1 == conta2)
conta1.deposita(10)
print(conta1 == conta2)

print('')

conta200 = ContaSalario(200)
conta200.deposita(1000)
conta300 = ContaSalario(300)
conta300.deposita(400)
conta400 = ContaSalario(400)
conta400.deposita(600)
contas_ordenadas = [conta200, conta300, conta400]

# for conta in sorted(contas_ordenadas, key=attrgetter('_saldo')):
for conta in sorted(contas_ordenadas):
    print(conta)

print('')

# Ordenação

idades = [15, 21, 65, 41, 47, 23, 29]
for i in range(len(idades)):
    print(i, idades[i])

print('')

for indice, idade in enumerate(idades):
    print(indice, idade)

print('')

sorted(idades)
print(idades)
