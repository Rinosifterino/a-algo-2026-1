import time
import sys

# Aumenta o limite de recursão para evitar RecursionError no n=1000
sys.setrecursionlimit(2000)

# Constante com os tamanhos solicitados
TAMANHOS_N = [10, 100, 500, 1000]


def calcular_fatorial(n):
    """
    Calcula o fatorial de um número n utilizando recursão.

    Args:
        n (int): O número a ser calculado.

    Returns:
        int: O resultado do fatorial de n.
    """
    # Caso base: o fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    
    # Passo recursivo: n multiplicado pelo fatorial de n-1
    return n * calcular_fatorial(n - 1)


def medir_tempos():
    #Mede o tempo de execução do algoritmo para a lista de tamanhos
    for n in TAMANHOS_N:
        inicio = time.time()
        calcular_fatorial(n)
        fim = time.time()
        
        tempo_total = fim - inicio
        print(f"Tempo para n={n:<4}: {tempo_total:.6f} segundos")


if __name__ == "__main__":
    medir_tempos()