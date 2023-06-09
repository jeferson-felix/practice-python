from bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('Teste', '01/01/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')


teste_idade()
