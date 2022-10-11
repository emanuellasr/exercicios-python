# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
valores = []
jogos = int(input('Quantos jogos você quer fazer? '))
sorteio =[]
total = 1
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in valores:
            valores.append(num)
            cont += 1
        if cont >= 6:
            break
    valores.sort()
    sorteio.append(valores[:])
    valores.clear()
    total += 1
for i, j in enumerate(sorteio):
    print(f'{i + 1}° JOGO: {j}')