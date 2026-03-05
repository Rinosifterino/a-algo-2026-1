import random
import time

TAMANHOS_N = [1000, 5000, 10000, 20000, 50000]

def insertion_sort(arr):
    lista = arr.copy()
    
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
        
    return lista

def comparar_algoritmos():
    for n in TAMANHOS_N:
        print(f"\n--- Testando para n = {n} ---")
        
        lista_aleatoria = [random.randint(0, 100000) for _ in range(n)]
        
        inicio_insertion = time.time()
        insertion_sort(lista_aleatoria)
        fim_insertion = time.time()
        
        inicio_timsort = time.time()
        sorted(lista_aleatoria)
        fim_timsort = time.time()
        
        print(f"Tempo Insertion Sort O(n^2): {fim_insertion - inicio_insertion:.4f}s")
        print(f"Tempo Python sorted() O(n log n): {fim_timsort - inicio_timsort:.4f}s")

if __name__ == "__main__":
    comparar_algoritmos()