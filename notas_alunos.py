# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.
aluno = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota I: '))
    n2 = float(input('Nota II: '))
    media = (n1+n2)/2
    aluno.append([nome, [n1, n2], media])
    resp = input('Quer continuar?[S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'{"N°:":<4} {"NOME: ":<10} {"MÉDIA":>8}')
for i, n in enumerate(aluno):
    print(f'{i + 1:<4} {n[0]:<10} {n[2]:>8}')
while True:
    escolha = int(input('Mostrar notas de qual aluno?[00 para sair]'))
    if escolha == 00:
        break
    if escolha <= len(aluno) - 1:
        print(f'Notas de {aluno[escolha][0]}: {aluno[escolha][1]}')
