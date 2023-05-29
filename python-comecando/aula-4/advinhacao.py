print(f'{"-"*35}')
print('Bem vindo ao jogo de adivinhação')
print(f'{"-"*35}')

numero_secreto = 40
tentativas = 3

while tentativas > 0:
    print(f'Tentativas disponíveis: {tentativas}')

    chute = int(input('Digite o seu número: '))

    print(f'Você digitou o número {chute}')

    if numero_secreto == chute:
        print('Você acertou!')
    else:
        if chute > numero_secreto:
            print(f'Você errou!, O seu chute foi maior que o número secreto.')
        elif chute < numero_secreto:
            print(f'Você errou!, O seu chute foi menor que o número secreto.')
    tentativas = tentativas - 1

print('Fim de jogo.')
