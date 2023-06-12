class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


carros = Filme('carros', 2006, 117)
carros.dar_like()
print(f'{carros.nome} - {carros.ano} - {carros.duracao} - {carros.likes}')

bb = Serie('breaking bad', 2008, 5)
bb.dar_like()
print(f'{bb.nome} - {bb.ano} - {bb.temporadas} - {bb.likes}')
