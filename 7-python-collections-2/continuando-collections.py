usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
# assistiram = usuarios_data_science.copy() | usuarios_machine_learning.copy()

print(usuarios_data_science.copy() | usuarios_machine_learning.copy())
print(usuarios_data_science.copy() & usuarios_machine_learning.copy())
print(usuarios_data_science.copy() - usuarios_machine_learning.copy())
print(usuarios_data_science.copy() ^ usuarios_machine_learning.copy())

print('')

usuarios = {1, 5, 76, 34, 52, 13, 17}
usuarios.add(765)
usuarios = frozenset(usuarios)
print(len(usuarios))

print('')

meu_texto = 'Em linguística a noção de texto é ampla e ainda aberta a uma definição mais precisa'

print(set(meu_texto.split()))
