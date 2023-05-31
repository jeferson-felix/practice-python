def jogar():
    palavra_secreta = "processador"
    acertou = False
    enforcou = False

    print(f'{"-" * 40}')
    print(f'{"Bem vindo ao jogo da forca":^40}')
    print(f'{"-" * 40}')

    while not enforcou and not acertou:
        print('Jogando')

    print('Fim de jogo.')


if __name__ == "__main__":
    jogar()
