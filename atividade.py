print('-=-'*10)
print('Cadastro')
print('-=-'*10)
total18 = totalM = totalF20 = 0
while True:
    idade = int(input('Qual a idade da pessoa? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Qual o sexo da pessoa?[M/F] ').strip().upper()[0]
    if idade > 18:
        total18 += 1
    if sexo == 'M':
        totalM += 1
    if sexo == 'F' and idade < 20:
        totalF20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar?[S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas menores de 18 anos cadastradas foi de {total18} pessoa(s).')
print(f'O total de homens cadastrados foi de {totalM} homens.')
print(f'O total de mulheres menores de 20 anos cadastradas foi de {totalM} mulher(es).')
