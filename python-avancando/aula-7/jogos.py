import forca
import advinhacao


def escolhe_jogo():
    print(f'{"-"*40}')
    print(f'{"Escolha seu jogo":^40}')
    print(f'{"-"*40}')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Escolha o jogo desejado: '))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()
    elif jogo == 2:
        print('Jogando Adivinhação')
        advinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
