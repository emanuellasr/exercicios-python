#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = contmil = menor = cont = 0
barato = ''
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    cont += 1
    total += preco
    if preco > 1000:
         contmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar?[S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'O total das compras em reais foi igual a {total}')
print(f'Um total de {contmil} produto(s) custaram mais de R$ 1.000 reais')
print(f'O produto mais barato foi {barato} de R${menor:.2f} reais.')


