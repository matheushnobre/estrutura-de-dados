from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')

for i in range(3):
    print('Removendo', queue.popleft())