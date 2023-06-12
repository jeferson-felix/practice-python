print(f'{"-"*35}')
print('Bem vindo ao jogo de adivinhação')
print(f'{"-"*35}')

numero_secreto = 40
tentativas = 4

for rodada in range(1, tentativas):
    print(f'Tentativa {rodada} de {tentativas - 1}')

    chute = int(input('Digite o seu número entre 1 e 100: '))

    print(f'Você digitou o número {chute}')

    if chute < 1 or chute > 100:
        print('Errou! Você deve digitar um número entre 1 e 100.')
        continue

    if numero_secreto == chute:
        print('Você acertou!')
        break
    else:
        if chute > numero_secreto:
            print(f'Você errou!, O seu chute foi maior que o número secreto.')
        elif chute < numero_secreto:
            print(f'Você errou!, O seu chute foi menor que o número secreto.')

print('Fim de jogo.')
