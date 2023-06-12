import re  # Regular Expression

endereco = 'Rua Vergueiro, 3185 - Vila Mariana, São Paulo - SP, 04101-300'

# padrão = 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile('[0-9]{5}-?[0-9]{3}')

busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
