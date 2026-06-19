from itertools import combinations
import time

def subset_sum(S, T):
    """
    Verifica a existência de um subconjunto de S cuja soma é T.
    Utiliza o algoritmo Meet-in-the-Middle para suportar arrays maiores.
    """
    n = len(S)
    mid = n // 2
    left, right = S[:mid], S[mid:]

    def get_sums(arr):
        sums = {0: []} # A soma de um subconjunto vazio é 0
        for r in range(1, len(arr) + 1):
            for combo in combinations(arr, r):
                sums[sum(combo)] = list(combo)
        return sums

    left_sums = get_sums(left)
    right_sums = get_sums(right)

    # Verifica se existe a soma correspondente na segunda metade
    for l_sum, l_subset in left_sums.items():
        r_target = T - l_sum
        if r_target in right_sums:
            final_subset = l_subset + right_sums[r_target]
            if len(final_subset) > 0: # Garante a exclusão do caso trivial vazio
                return final_subset
                
    return None

# ==========================================
# EXIBIÇÃO DE INPUT E OUTPUT DOS CENÁRIOS
# ==========================================

print("=== Cenário 1: Tamanho Pequeno ===")
S1, T1 = [2, 4, 6, 10], 16
print(f"Input : S = {S1} | T = {T1}")
print(f"Output: {subset_sum(S1, T1)}\n")

print("=== Cenário 2: Tamanho Médio ===")
S2, T2 = [-5, -2, 1, 3, 7, 12, 15, 21], 0
print(f"Input : S = {S2} | T = {T2}")
print(f"Output: {subset_sum(S2, T2)}\n")

print("=== Cenário 3: Tamanho Grande ===")
# Gerando 30 inteiros de 5 dígitos (incluindo uma combinação intencional que soma 500.000)
S3_base = [85000, 85000, 85000, 85000, 85000, 75000] # Subconjunto que soma exatos 500.000
S3_filler = [12345, 87654, 43210, 11111, 22222, 33333, 44444, 55555, 66666, 77777,
             88888, 10101, 20202, 30303, 40404, 50505, 60606, 70707, 80808, 90909,
             13579, 24680, 97531, 86420]
S3 = S3_base + S3_filler
T3 = 500000

print(f"Input : S possui {len(S3)} inteiros de cinco dígitos | T = {T3}")

# Medição de tempo para provar a eficiência da estratégia
start_time = time.time()
resultado3 = subset_sum(S3, T3)
end_time = time.time()

print(f"Output: {resultado3}")
print(f"Tempo de execução: {(end_time - start_time):.5f} segundos")