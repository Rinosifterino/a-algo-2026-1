import random
import math
import matplotlib.pyplot as plt

# ==========================================
# 1. UTILIDADES (Substitui seu nqueens_utils.py)
# ==========================================
def calcula_custos(estado):
    """Calcula o número de pares de rainhas se atacando (Fitness). O ideal é 0."""
    ataques = 0
    n = len(estado)
    for i in range(n):
        for j in range(i + 1, n):
            # Verifica se estão na mesma linha ou mesma diagonal
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                ataques += 1
    return ataques

def gera_vizinho(estado):
    """Gera um estado vizinho movendo uma rainha aleatória para uma nova linha."""
    vizinho = list(estado)
    n = len(estado)
    coluna = random.randint(0, n - 1)
    nova_linha = random.randint(0, n - 1)
    
    # Garante que a rainha realmente mudou de lugar
    while nova_linha == estado[coluna]:
        nova_linha = random.randint(0, n - 1)
        
    vizinho[coluna] = nova_linha
    return vizinho

def estado_inicial(n=12):
    """Gera um tabuleiro aleatório com 1 rainha por coluna."""
    return [random.randint(0, n - 1) for _ in range(n)]

# ==========================================
# 2. LOOP DO SIMULATED ANNEALING (A Tarefa)
# ==========================================
def simulated_annealing(n=12, temp_inicial=100.0, alfa=0.99, max_iteracoes=10000):
    """
    INPUTS:
    - n: Tamanho do tabuleiro (12 rainhas)
    - temp_inicial: Temperatura inicial do sistema
    - alfa: Taxa de resfriamento (cooling rate)
    """
    estado_atual = estado_inicial(n)
    custo_atual = calcula_custos(estado_atual)
    temp = temp_inicial
    
    historico_custos_sa = [custo_atual]
    
    for i in range(max_iteracoes):
        # OUTPUT: Condição de parada de sucesso
        if custo_atual == 0:
            print(f"Solução encontrada na iteração {i}!")
            break
            
        vizinho = gera_vizinho(estado_atual)
        custo_vizinho = calcula_custos(vizinho)
        
        # Diferença de energia (custo)
        delta_e = custo_vizinho - custo_atual
        
        # Critério de Aceitação (Metrópolis)
        # Aceita se for melhor (delta_e < 0) OU com base na probabilidade da temperatura
        if delta_e < 0 or random.random() < math.exp(-delta_e / max(temp, 1e-10)):
            estado_atual = vizinho
            custo_atual = custo_vizinho
            
        historico_custos_sa.append(custo_atual)
        
        # Resfriamento
        temp *= alfa
        
    return estado_atual, custo_atual, historico_custos_sa

# ==========================================
# 3. EXECUÇÃO E GERAÇÃO DO GRÁFICO (Output)
# ==========================================
if __name__ == "__main__":
    print("--- Iniciando Simulated Annealing (12-Rainhas) ---")
    
    # Executa o SA
    estado_final, custo_final, historico_sa = simulated_annealing()
    
    print(f"Estado Final (linhas por coluna): {estado_final}")
    print(f"Custo Final (Conflitos): {custo_final}")
    
    # MOCK DO AG: Substitua esta lista pelo histórico real do seu Algoritmo Genético!
    # Estou gerando um decaimento linear falso apenas para o código funcionar e plotar.
    historico_ag_seu_codigo = [max(0, historico_sa[0] - (i * 0.05)) for i in range(len(historico_sa))]

    # Plotando as Curvas de Convergência
    plt.figure(figsize=(10, 6))
    plt.plot(historico_sa, label='Simulated Annealing (SA)', color='blue', linewidth=2)
    plt.plot(historico_ag_seu_codigo, label='Algoritmo Genético (AG)', color='orange', linestyle='--')
    
    plt.title('Convergência: Simulated Annealing vs Algoritmo Genético (12-Rainhas)')
    plt.xlabel('Iterações / Avaliações')
    plt.ylabel('Custo (Número de Conflitos)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()