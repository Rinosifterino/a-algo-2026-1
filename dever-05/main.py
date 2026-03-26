# 1) Algoritmo de ordenação Merge Sort

# Teoria: O algoritmo adota a estratégia "dividir para conquistar". 
# Ele divide o array pela metade até atingir elementos únicos
# e depois junta (merge) essas metades ordenando-as.
# Complexidade: O(n log n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
    return arr

# 2) Multiplicação de matrizes

# Teoria: A multiplicação de duas matrizes quadradas de tamanho n x n 
# multiplica cada linha por cada coluna. 
# Complexidade: O(n³)

def multiplicacao_matrizes(matriz_a, matriz_b):
    n = len(matriz_a)
    matriz_c = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]
                
    return matriz_c


# ==========================================
# 3) Recorrências:
# ==========================================
# O Teorema Mestre é usado para encontrar a complexidade usando T(n) = aT(n/b) + f(n).
"""
a) T(n) = 2T(n/4) + √n
    - a = 2, b = 4, f(n) = n^(1/2)
    - n^(log_b(a)) = n^(log_4(2)) = n^(1/2)
    - f(n) é igual a n^(log_b(a)), Caso 2 do Teorema Mestre.
    -> Complexidade: Θ(√n * log n)

b) T(n) = 2T(n/4) + n
    - a = 2, b = 4, f(n) = n^1
    - n^(log_b(a)) = n^(log_4(2)) = n^(0.5)
    - f(n) cresce mais rápido que n^(0.5), Caso 3 do Teorema Mestre.
    -> Complexidade: Θ(n)

c) T(n) = 16T(n/4) + n²
    - a = 16, b = 4, f(n) = n²
    - n^(log_b(a)) = n^(log_4(16)) = n²
    - f(n) é igual a n^(log_b(a)), Caso 2 do Teorema Mestre.
    -> Complexidade: Θ(n² * log n)
"""