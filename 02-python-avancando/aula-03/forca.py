def jogar():
    palavra_secreta = 'carro'.upper()
    acertou = False
    enforcou = False
    letras_acertadas = ['_', '_', '_', '_', '_']

    print(f'{"-" * 40}')
    print(f'{"Bem vindo ao jogo da forca":^40}')
    print(f'{"-" * 40}')

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input('Qual letra? ').strip().upper()

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print('Fim de jogo.')


if __name__ == "__main__":
    jogar()
