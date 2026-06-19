import heapq

def prim_mst(grafo, vertice_inicial):
    mst = []
    visitados = set([vertice_inicial])
    
    # Inicializa a fila de prioridade com as arestas do vértice inicial
    # Formato: (peso, origem, destino)
    arestas = [
        (peso, vertice_inicial, destino)
        for destino, peso in grafo[vertice_inicial].items()
    ]
    heapq.heapify(arestas)
    
    custo_total = 0

    while arestas:
        # Pega a aresta de menor peso disponível
        peso, origem, destino = heapq.heappop(arestas)
        
        # Se o destino ainda não foi visitado, incluímos na MST
        if destino not in visitados:
            visitados.add(destino)
            mst.append((origem, destino, peso))
            custo_total += peso
            
            # Adiciona as novas arestas do vértice recém-descoberto à fila
            for proximo_destino, proximo_peso in grafo[destino].items():
                if proximo_destino not in visitados:
                    heapq.heappush(arestas, (proximo_peso, destino, proximo_destino))

    return custo_total, mst

# --- INPUT EXPLÍCITO ---
# Representação do grafo da imagem usando um dicionário de adjacências
grafo = {
    'A': {'B': 2, 'C': 6, 'D': 3},
    'B': {'A': 2, 'D': 5},
    'C': {'A': 6, 'D': 4},
    'D': {'A': 3, 'B': 5, 'C': 4}
}

# --- EXECUÇÃO ---
# Rodando o algoritmo começando do vértice 'A'
custo_total, arestas_mst = prim_mst(grafo, 'A')

# --- OUTPUT EXPLÍCITO ---
print("-" * 40)
print(" RESULTADO DO ALGORITMO DE PRIM")
print("-" * 40)
print(f"Custo Total da Árvore Geradora Mínima: {custo_total}\n")
print("Arestas Componentes:")
print(f"{'Origem':<10} | {'Destino':<10} | {'Peso':<5}")
print("-" * 40)
for origem, destino, peso in arestas_mst:
    print(f"Vértice {origem:<2} | Vértice {destino:<2} | {peso:<5}")
print("-" * 40)