def jogar():
    palavra_secreta = 'carro'.upper()
    acertou = False
    enforcou = False
    erros = 0
    letras_acertadas = ['_' for letra in palavra_secreta]

    print(f'{"-" * 40}')
    print(f'{"Bem vindo ao jogo da forca":^40}')
    print(f'{"-" * 40}')

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input('Qual letra? ').strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6

        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print('Fim de jogo. Você venceu!')
    else:
        print('Fim de jogo. Você perdeu!')


if __name__ == "__main__":
    jogar()
