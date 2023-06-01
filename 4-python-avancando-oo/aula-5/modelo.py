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

    def __str__(self):
        return f'{self._nome} - {self.ano} -  {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


carros = Filme('carros', 2006, 117)
carros.dar_like()

intr = Filme('interestelar', 2014, 169)
intr.dar_like()

bb = Serie('breaking bad', 2008, 5)
bb.dar_like()

drk = Serie('dark', 2017, 3)
drk.dar_like()

filmes_e_series = [carros, intr, bb, drk]

playlist_fds = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fds)}')

for programa in playlist_fds:
    print(programa)
