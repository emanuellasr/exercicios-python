#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numero = ('''zero', 'um', 'dois', 'trÊs', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte''')
while True:
    escolha = int(input('Escolha um número entre 0  e 20: '))
    if 0 <= escolha <= 20:
        break
    else:
        print('Comando inválido! Digite um número entre 0 e 20: ')
print(f'Você escolheu o número {numero[escolha]}')
