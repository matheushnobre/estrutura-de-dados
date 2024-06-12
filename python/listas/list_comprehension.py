# Criando uma lista com list comprehension
lista = [numero for numero in range(10)]
print(lista)
print(50*'-')

# Mapeamento de dados com list comprehension
# Aumentando os preços dos nossos produtos em 10%
produtos = [
    {'produto': 'arroz 1kg', 'preco': 5.87}, 
    {'produto': 'patinho/kg', 'preco': 37.99}, 
    {'produto': 'macarrão 500g', 'preco': 2.75}
]

produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
]

print(*produtos, sep='\n')
print(50*'-')

# Filtro de dados
lista = [n for n in range(10) if n % 2 == 0]
print(lista)
print(50*'-')

# Realizando novo reajuste na lista de produtos, agora de 5%, apenas no preço dos produtos acima de R$6,00
produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)} if produto['preco'] > 6 
    else {**produto}
    for produto in produtos
]

print(*produtos, sep='\n')
print(50*'-')

# List comprehension com mais de um for
lista = [(x, y) for x in range(3) for y in range(3)]
print(lista)