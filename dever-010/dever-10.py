def resolver_bellman_ford():
    # 1. INPUT: Definição explícita do grafo
    vertices = [0, 1, 2, 3, 4]
    
    # Lista de tuplas (origem, destino, peso)
    arestas = [
        (0, 1, 5),
        (1, 2, 1),
        (1, 3, 2),
        (2, 4, 1),
        (4, 3, -1)
    ]
    
    origem = 0
    V = len(vertices)

    print("=== INPUT: DADOS DO GRAFO ===")
    print(f"Vértices: {vertices}")
    print("Arestas (Origem -> Destino : Peso):")
    for u, v, p in arestas:
        print(f"  {u} -> {v} : {p}")
    print("="*30 + "\n")

    # Inicialização das distâncias e predecessores
    distancias = {v: float('inf') for v in vertices}
    predecessores = {v: None for v in vertices}
    distancias[origem] = 0

    # Função auxiliar para formatar a célula da tabela
    def formatar_celula(d, p):
        if d == float('inf'):
            return "(∞, -)"
        return f"({d}, {p if p is not None else '-'})"

    # 2. OUTPUT: Tabela de Iterações
    print("=== OUTPUT: TABELA DE ITERAÇÕES ===")
    print("Formato: (Distância Atual, Predecessor)")
    
    # Cabeçalho da tabela
    cabecalho = f"{'Passo':<12} | " + " | ".join([f"Vértice {v:<4}" for v in vertices])
    print("-" * len(cabecalho))
    print(cabecalho)
    print("-" * len(cabecalho))

    # Imprimir Iteração 0 (Estado inicial)
    linha = [formatar_celula(distancias[v], predecessores[v]) for v in vertices]
    linha_str = f"{'Inicial (0)':<12} | " + " | ".join([f"{cel:<9}" for cel in linha])
    print(linha_str)

    # Executar as iterações (V - 1 vezes)
    for i in range(1, V):
        # Cria cópias para garantir que o resultado dependa apenas do estado da iteração anterior
        novas_distancias = distancias.copy()
        novos_predecessores = predecessores.copy()
        
        for u, v, peso in arestas:
            if distancias[u] != float('inf') and distancias[u] + peso < novas_distancias[v]:
                novas_distancias[v] = distancias[u] + peso
                novos_predecessores[v] = u
                
        distancias = novas_distancias
        predecessores = novos_predecessores

        # Imprimir linha da iteração atual
        linha = [formatar_celula(distancias[v], predecessores[v]) for v in vertices]
        linha_str = f"Iteração {i:<4} | " + " | ".join([f"{cel:<9}" for cel in linha])
        print(linha_str)
        
    print("-" * len(cabecalho) + "\n")

    # 3. OUTPUT: Verificação de Ciclo Negativo
    print("=== OUTPUT: VERIFICAÇÃO DE CICLO NEGATIVO ===")
    tem_ciclo_negativo = False
    
    # Se conseguirmos relaxar mais uma aresta após V-1 iterações, há um ciclo negativo
    for u, v, peso in arestas:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            tem_ciclo_negativo = True
            break

    if tem_ciclo_negativo:
        print("Resultado: EXISTE um ciclo negativo no grafo.")
    else:
        print("Resultado: NÃO EXISTE ciclo negativo no grafo.")

if __name__ == "__main__":
    resolver_bellman_ford()