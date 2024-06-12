produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dicionario = {
    chave: valor.upper() 
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
}

print(dicionario)