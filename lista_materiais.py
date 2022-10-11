# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
materiais = ('Lápis', 2.90,
             'Borracha', 7.60,
             'Prancheta', 20.00,
             'Caixa Organizadora', 73.00,
             'Marca Texto', 3.50,
             'Chamequinho', 14.70,
             'Fichário', 123.00,
             'Giz de Cera', 14.90,
             'Livro', 34.90,
             'Mochila', 100.00)
print('=' * 20)
print(f'{"LISTA DE MATERIAIS":^10}')
print('=' * 20)
for item in range(0, len(materiais)):
    if item % 2 == 0:
        print(f'{materiais[item]:.<30}', end=' ')
    elif item % 2 == 1:
        print(f'R${materiais[item]:>7.2f}')
