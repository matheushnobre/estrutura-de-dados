from pilha import Stack

def converter(decimal):
    if decimal == 0:
        return '0'
    
    s = Stack()
    while decimal > 0:
        s.push(decimal % 2)
        decimal = decimal // 2
    
    binario = ''
    while not s.isEmpty():
        binario += str(s.pop())
        
    return binario

for i in range(100):
    print(f'{i} em binário = {converter(i)}')