import random

numero_secreto = random.randint(1, 10)
tentativas = 0
pontos = 100

print(f'{"-"*35}')
print('Bem vindo ao jogo de adivinhação')
print(f'{"-"*35}')
print(f'{numero_secreto}')
print(f'Qual nível de dificuldade?')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Digite o nível escolhido: '))

if nivel == 1:
    tentativas = 6
elif nivel == 2:
    tentativas = 4
elif nivel == 3:
    tentativas = 2

for rodada in range(1, tentativas):
    print(f'Tentativa {rodada} de {tentativas - 1}')

    chute = int(input('Digite o seu número entre 1 e 10: '))

    print(f'Você digitou o número {chute}')

    if chute < 1 or chute > 100:
        print('Errou! Você deve digitar um número entre 1 e 10.')
        continue

    if numero_secreto == chute:
        print('Você acertou!')
        break
    else:
        if chute > numero_secreto:
            print(f'Você errou!, O seu chute foi maior que o número secreto.')
        elif chute < numero_secreto:
            print(f'Você errou!, O seu chute foi menor que o número secreto.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print(f'Você terminou com {pontos} pontos!')
print('Fim de jogo.')
