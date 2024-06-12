from pilha import Stack

def checar(expressao):
    s = Stack()
    balanceado = True
    index = 0
    
    while index < len(expressao) and balanceado:
        parentese = expressao[index]
        if parentese == "(":
            s.push(parentese)
        else:
            if s.isEmpty():
                balanceado = False
            else:
                s.pop()

        index += 1

    if balanceado and s.isEmpty():
        return True
    else:
        return False
    
while True:
    expressao = input('\nDigite a expressão: ')
    if expressao == '':
        break
    print('Expressão balanceada') if checar(expressao) else print('Expressão NÃO balanceada')