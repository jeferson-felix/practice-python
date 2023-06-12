import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametros = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametros + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == - 1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'Parâmetros: ' + self.get_url_parametros() + '\n' + 'URL Base: ' \
            + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

    def conversao(self, moeda_origem, moeda_destino, quantidade):
        if moeda_origem == 'real' and moeda_destino == 'dolar' and quantidade > 0:
            return quantidade / valor_dolar
        elif moeda_origem == 'dolar' and moeda_destino == 'real' and quantidade > 0:
            return quantidade * valor_dolar
        else:
            raise ValueError('Parâmetros Inválidos')


extrator_url = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
extrator_url2 = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
valor_quantidade = extrator_url.get_valor_parametro('moedaDestino')
valor_dolar = 4.96
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')
conversao = extrator_url.conversao(moeda_origem, moeda_destino, float(quantidade))

print(extrator_url)
print(f'Tamanho da URL: {len(extrator_url)}')
print(f'URL 1 é igual a URL 2?: {extrator_url == extrator_url}')
print(f'Quantidade: {float(quantidade):.2f} ({moeda_origem})\nConversão: {conversao:.2f} ({moeda_destino})')
