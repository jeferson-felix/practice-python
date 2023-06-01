class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


carros = Filme('carros', 2006, 117)
carros.dar_like()
print(f'Nome: {carros.nome} - Ano: {carros.ano} - Duração: {carros.duracao} - Likes: {carros.likes}')

bb = Serie('breaking bad', 2008, 5)
bb.dar_like()
print(f'Nome: {bb.nome} - Ano: {bb.ano} - Temporadas: {bb.temporadas} - Likes: {bb.likes}')
