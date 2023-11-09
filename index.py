import heapq
import random
n, m = input().split()
n = int(n) #numero de vertices
m = int(m) #numero de arestas
H = [] # fila de prioridade
n_out = [[]*n for i in range(n)] # n listas de vizinhos, uma para cada nó
for j in range(m): # ler as arestas do digrafo
 a, b, c = input().split() # ler as arestas de a para b com o custo
 a = int(a)
 b = int(b)
 c = int(c)
 n_out[a].append((b,c)) # colocar vizinhos na lista do vertice
 n_out[b].append((a,c))
raiz = random.randint(0, n-1)
for (x,c) in n_out[raiz]:
 heapq.heappush(H, (c, raiz, x)) # [(2, 0, 2), (5, 0, 1)]
n_edges = 0 #numero de arestas marcadas
custo_tot = 0
marcados = [raiz] #lista de nós marcados
arv_ger_min = []
while n_edges < n-1:
 while True: #encontrar uma aresta que não foi marcada
   (c, a, b) = heapq.heappop(H)
   if b not in marcados:
     break
 marcados.append(b)
 print(a, b)
 print(marcados)
 custo_tot += c
 arv_ger_min.append((a, b))
 n_edges += 1
 for (x,c) in n_out[b]:
   if x not in marcados:
     heapq.heappush(H,(c,b,x))
print(custo_tot)
print(arv_ger_min)