idades = [18, 22, 31, 14]

idades.remove(31)
idades.append(35)
idades.extend([44, 51])

for idade in idades:
    print(idade)
print('')

idades_prox_ano = []
for idade in idades:
    idades_prox_ano.append(idade+1)
print(idades_prox_ano, '\n')

idades_prox_ano1 = [(idade+1) for idade in idades]
print(idades_prox_ano1, '\n')

idade_maior_21 = [idade for idade in idades if idade > 21]
print(idade_maior_21)
