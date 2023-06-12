from cpf_cnpj import Documento
from telefones_br import TelefonesBR
from datas import DatasBR
from acesso_cep import BuscaEndereco

# Exemplos
exemplo_cpf = "14203643082"
exemplo_cnpj = "41217267000112"
exemplo_telefone = "5511956716541"
exemplo_cep = "04101300"

# Criando objetos
documento_cpf = Documento.cria_documento(exemplo_cpf)
documento_cnpj = Documento.cria_documento(exemplo_cnpj)
telefone_objeto = TelefonesBR(exemplo_telefone)
cadastro = DatasBR()
cep_objeto = BuscaEndereco(exemplo_cep)
acesso = cep_objeto.acessa_via_cep()
bairro, cidade, uf = cep_objeto.acessa_via_cep()

# Print objetos
print(f'CPF: {documento_cpf}')
print(f'CNPJ: {documento_cnpj}\n')

print(f'Telefone: {telefone_objeto}\n')

print(f'Data do cadastro: {cadastro}')
print(f'Tempo de cadastro: {cadastro.tempo_cadastro()}\n')

print(f'CEP: {cep_objeto}')
print(f'Bairro: {bairro}, Cidade: {cidade}, UF: {uf}')
