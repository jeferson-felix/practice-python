from cpf_cnpj import Documento
from telefones_br import TelefonesBR

# Exemplos
exemplo_cpf = "14203643082"
exemplo_cnpj = "41217267000112"
exemplo_telefone = "5511956716541"

# Criando objetos
documento_cpf = Documento.cria_documento(exemplo_cpf)
documento_cnpj = Documento.cria_documento(exemplo_cnpj)
telefone_objeto = TelefonesBR(exemplo_telefone)

# Print objetos
print(documento_cpf)
print(documento_cnpj)
print(telefone_objeto)
