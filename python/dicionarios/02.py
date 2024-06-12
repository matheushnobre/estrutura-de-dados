# Faça um programa, utilizando dicionários, que peça para o usuário inserir o nome de três produtos de 
# mercado e seus respectivos preços e os mostre na tela

produtos= dict()
print('LISTA DE COMPRAS')
for i in range(3):
    produto = input('Produto: ')
    preco = input('Preço: R$')
    produtos[produto] = preco
    
print(produtos)
