s1 = set() # vazio
s1 = {'Matheus', 1, 2, 3} # com dados
#print(s1)

# sets são eficientes para remover valores duplicados de iteráveis
l1 = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 6, 7]
l1 = list(set(l1))
#print(l1)

# observações: 
# seus valores serão sempre únicos
# não aceitam valores mutáveis
# não tem indexes
# não garantem ordem
# são iteráveis

# métodos úteis
s1.add('Matheus') # adiciona
s1.update('Olá mundo') # adiciona iterando
s1.discard('Matheus') # elimina valor
s1.clear() # limpa o set

# operadores úteis (conjuntos)
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # união (union)
print("União", s3)
s3 = s1 & s2 # interseção (intersection)
print("Interseção", s3)
s3 = s1 - s2 # diferença (itens presentes apenas no set da esquerda)
print("Diferença", s3)
s3 = s1 ^ s2 # diferença simétrica (itens que não estão em ambos)
print("Diferença simétrica", s3)