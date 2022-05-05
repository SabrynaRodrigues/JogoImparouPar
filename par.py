# Jogo Ímpar ou Par 
# Sabryna Rodrigues - Desafio Curso em Vídeo Mundo Python

from random import randint
print('-=' * 40)
print('JOGO ÍMPAR OU PAR')
print("-=" * 40)
while True:
    n = int(input('Diga um valor:'))
    player = str(input('Escolha um: ímpar ou par?')).lower()
    comp = randint(0, 11)
    total = n + comp
    print('Você jogou o n {} e o computador jogou {}'.format(n, comp))
    if player == 'par':
        if total % 2 == 0:
            print('Você venceu!!')
        else:
            print('Perdeu!')
            break
    elif player == 'impar':
        if total % 2 == 1:
            print('Ganhou!')
        else:
            print('Perdeu!')
            break
    print('VAMOS JOGAR DE NOVO!')