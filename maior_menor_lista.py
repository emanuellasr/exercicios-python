#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
maior = menor = 0
for num in range(0,5):
    valores.append(int(input(f'Insira um número para a posição {num}: ')))
    if num == 0:
        maior = menor = valores[num]
    else:
        if valores[num] > maior:
            maior = valores[num]
        if valores[num] < menor:
            menor = valores[num]
print(f'Você digitou os valores {valores}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número dogitado foi {menor}')