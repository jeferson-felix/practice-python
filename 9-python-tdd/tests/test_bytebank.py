from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_01_01_2000_deve_retornar_23(self):
        entrada = '01/01/2000'  # Given
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1000)
        resultado = funcionario_teste.idade()  # When

        assert resultado == esperado  # Then

    def test_quando_sobrenome_recebe_Jeferson_Felix_deve_retornar_Felix(self):
        entrada = 'Jeferson Felix'  # Given
        esperado = 'Felix'

        jeferson = Funcionario(entrada, '24/07/2002', 1000)
        resultado = jeferson.sobrenome()  # When

        assert resultado == esperado  # Then

    def test_quando_decrecimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '01/01/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado
