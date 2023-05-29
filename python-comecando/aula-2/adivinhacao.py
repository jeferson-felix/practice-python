print(f'{"-"*35}')
print('Bem vindo ao jogo de adivinhação')
print(f'{"-"*35}')

numero_secreto = 40

chute = int(input('Digite o seu número: '))

print(f'Você digitou o número {chute}')

if numero_secreto == chute:
    print('Você acertou!')
else:
    print(f'Você errou!, o número secreto era {numero_secreto}')
