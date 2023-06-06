usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
# assistiram = usuarios_data_science.copy() | usuarios_machine_learning.copy()

print(usuarios_data_science.copy() | usuarios_machine_learning.copy())
print(usuarios_data_science.copy() & usuarios_machine_learning.copy())
print(usuarios_data_science.copy() - usuarios_machine_learning.copy())
print(usuarios_data_science.copy() ^ usuarios_machine_learning.copy())
