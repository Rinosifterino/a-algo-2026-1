import math

# ==========================================
# 1. INPUT (Descrição do Problema)
# ==========================================
# Grafo direcionado com vértices e pesos das arestas
grafo = {
    0: {1: 4, 2: 1},
    1: {3: 1},
    2: {1: 2, 4: 5},
    3: {4: 1},
    4: {}
}

inicio = 0
destino = 4

# ==========================================
# 2. EXECUÇÃO DO ALGORITMO
# ==========================================
def dijkstra(grafo, inicio, destino):
    # Inicialização
    distancias = {no: math.inf for no in grafo}
    predecessores = {no: None for no in grafo}
    distancias[inicio] = 0
    nao_visitados = list(grafo.keys())

    print("--- EXECUÇÃO PASSO A PASSO ---")
    print(f"{'Nó Visitado':<12} | {'Distâncias (0, 1, 2, 3, 4)':<35} | {'Predecessores (Nó:Origem)'}")
    print("-" * 80)

    while nao_visitados:
        # Extrai o nó não visitado com a menor distância
        no_atual = min(nao_visitados, key=lambda no: distancias[no])
        
        # Formatação para a tabela (mostra o estado ANTES de atualizar os vizinhos do nó atual)
        dists_str = ", ".join([f"{n}: {d if d != math.inf else '∞'}" for n, d in distancias.items()])
        preds_str = ", ".join([f"{n}:{p}" for n, p in predecessores.items() if p is not None])
        print(f"Avaliando: {no_atual:<2} | {dists_str:<35} | {preds_str}")

        # Se o destino for alcançado ou o menor for infinito (inacessível)
        if distancias[no_atual] == math.inf or no_atual == destino:
            break

        nao_visitados.remove(no_atual)

        # Atualiza distâncias dos vizinhos
        for vizinho, peso in grafo[no_atual].items():
            if vizinho in nao_visitados:
                nova_distancia = distancias[no_atual] + peso
                # Relaxamento da aresta
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = no_atual

    # ==========================================
    # 3. OUTPUT FINAL (Reconstrução da Rota)
    # ==========================================
    caminho = []
    no_passo = destino
    while no_passo is not None:
        caminho.insert(0, no_passo)
        no_passo = predecessores[no_passo]

    print("-" * 80)
    print("\n--- RESULTADO FINAL ---")
    print(f"Caminho mínimo percorrido: {' -> '.join(map(str, caminho))}")
    print(f"Custo mínimo total: {distancias[destino]}")

# Chama a função
dijkstra(grafo, inicio, destino)