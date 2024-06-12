# Faça um programa, utilizando dicionários, que peça para o usuário inserir quatro notas e mostre na tela as
# notas e a média entre elas

notas = dict()
for i in range(4):
    notas[f'Nota {i+1}'] = float(input(f'Insira a nota {i+1}: '))

media = sum(notas.values()) / 4
print('Notas:', notas)
print('Média:', media)