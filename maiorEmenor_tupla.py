#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.Depois disso, mostre a listagem de números
#gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),
           randint(1,10), randint(1,10))
print('Os números sorteados foram: ', end = '')
for num in numeros:
        print(f'{num}', end = ' ')
print(f'\nO maior número sorteado foi {max(numeros)}.')
print(f'O menor número sorteado foi {min(numeros)}.')