#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
vit = 0
from random import randint
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,11)
    tot = jogador + computador
    palpite = ' '
    while palpite not in 'PI':
        palpite = input('Par ou Ímpar?[P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}')
    print(f'Totalizando {tot}')
    if palpite == 'P':
        if tot % 2 == 0:
            print('Parabéns! Você venceu!')
            vit += 1
        else:
            print('Você perdeu!')
            break
    elif palpite == 'I':
        if tot % 2 == 1:
            print('Parabéns! Você venceu!')
            vit += 1
        else:
            print('Você perdeu!')
            break
