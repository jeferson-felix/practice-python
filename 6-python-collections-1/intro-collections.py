class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Código {self.codigo} Saldo {self.saldo}<<]"


conta_do_jef = ContaCorrente(15)
conta_do_jef.deposita(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
