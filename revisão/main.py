import time
import sys

# Aumenta limite de recursão para o fatorial
sys.setrecursionlimit(2000)

# 1. Fatorial Recursivo [cite: 3229, 4304, 5508]
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# 2. Fibonacci Recursivo [cite: 4306, 5016]
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3. Pesquisa Binária Recursiva [cite: 6350]
def pesquisa_binaria_recursiva(lista, alvo, baixo, alto):
    if baixo > alto:
        return -1
    meio = (baixo + alto) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return pesquisa_binaria_recursiva(lista, alvo, meio + 1, alto)
    else:
        return pesquisa_binaria_recursiva(lista, alvo, baixo, meio - 1)

# 4. Torre de Hanói [cite: 6437]
# (Prints originais omitidos para não poluir a saída e aferir o tempo puro de recursão)
def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        return
    torre_de_hanoi(n - 1, origem, auxiliar, destino)
    torre_de_hanoi(n - 1, auxiliar, destino, origem)

def medir_tempo(nome_algoritmo, funcao, *args):
    inicio = time.perf_counter()
    funcao(*args)
    fim = time.perf_counter()
    print(f"{nome_algoritmo}: {fim - inicio:.6f} segundos")

if __name__ == "__main__":
    print("--- Tempo de Execução dos Algoritmos ---")
    
    medir_tempo("Fatorial (n=500)", fatorial, 500)
    medir_tempo("Fibonacci (n=30)", fibonacci, 30)
    
    lista = list(range(1000000))
    medir_tempo("Pesquisa Binária (n=1M)", pesquisa_binaria_recursiva, lista, 999999, 0, len(lista)-1)
    
    medir_tempo("Torre de Hanói (n=20)", torre_de_hanoi, 20, 'A', 'C', 'B')