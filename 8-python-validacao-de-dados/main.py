from cpf_cnpj import Documento

exemplo_cpf = "14203643082"
exemplo_cnpj = "41217267000112"

documento_cpf = Documento.cria_documento(exemplo_cpf)
documento_cnpj = Documento.cria_documento(exemplo_cnpj)

print(documento_cpf)
print(documento_cnpj)
