# Heap: é uma arvore binária, usada para encontrar os maiores e menores valores mais rapidamente
# Min heap - o menor está no topo
# max-heap - O maior está no topo

import heapq

heap = []

# Adicionando elementos:
while True:
    num = int(input('Qual numero?'))
    if num != 0:
        heapq.heappush(heap, num)
        print(heap)
    else:
        break

# Ele sempre vai deixar o menor elemento no índice 0