def jogar():
    palavra_secreta = 'processador'.upper()
    acertou = False
    enforcou = False

    print(f'{"-" * 40}')
    print(f'{"Bem vindo ao jogo da forca":^40}')
    print(f'{"-" * 40}')

    while not enforcou and not acertou:

        chute = input('Qual letra? ').strip().upper()

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f'Encontrei a letra {letra} na posição {index}')
            index = index + 1

        print('Jogando')

    print('Fim de jogo.')


if __name__ == "__main__":
    jogar()
