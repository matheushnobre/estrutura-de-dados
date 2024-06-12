from pilha import Stack

def checar(expressao):
    s = Stack()
    abertura = '{[('
    fechamento = "}])"
    index = 0
    balanceado = True
    
    while index < len(expressao) and balanceado:
        simbolo = expressao[index]
        if simbolo in abertura:
            s.push(simbolo)
        else:
            if s.isEmpty(): 
                balanceado = False
            ultimo = s.pop()
            if abertura.index(ultimo) != fechamento.index(simbolo):
                balanceado = False
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