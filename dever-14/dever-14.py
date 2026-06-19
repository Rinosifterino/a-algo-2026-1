import math
from collections import Counter

# ==========================================
# 1. INPUTS
# ==========================================
# Base de dados de treino: [Salário, Crédito, Perfil, Nome]
dados_treino = [
    {"nome": "Ana", "salario": 40, "credito": 20, "perfil": "Conservador"},
    {"nome": "Bruno", "salario": 50, "credito": 35, "perfil": "Conservador"},
    {"nome": "Carlos", "salario": 90, "credito": 90, "perfil": "Agressivo"},
    {"nome": "Diana", "salario": 80, "credito": 65, "perfil": "Agressivo"}
]

# Dados do novo cliente a ser classificado
arthur = {"nome": "Arthur", "salario": 60, "credito": 45}

# Parâmetro k
k = 3

print("--- INPUTS ---")
for d in dados_treino:
    print(f"Treino -> {d['nome']}: Salário={d['salario']}, Crédito={d['credito']} | Perfil={d['perfil']}")
print(f"Alvo   -> {arthur['nome']}: Salário={arthur['salario']}, Crédito={arthur['credito']}")
print(f"k      = {k}\n")

# ==========================================
# 2. PROCESSAMENTO (KNN)
# ==========================================
distancias = []

# Calcular a distância euclidiana de Arthur para todos os clientes na base
for d in dados_treino:
    distancia = math.sqrt((d['salario'] - arthur['salario'])**2 + (d['credito'] - arthur['credito'])**2)
    distancias.append((distancia, d['perfil'], d['nome']))

# Ordenar a lista pelas menores distâncias (ordem crescente)
distancias.sort()

# Pegar apenas os 'k' primeiros (vizinhos mais próximos)
vizinhos_proximos = distancias[:k]

# Contar qual perfil aparece mais vezes entre os k vizinhos
perfis_vizinhos = [vizinho[1] for vizinho in vizinhos_proximos]
perfil_vencedor = Counter(perfis_vizinhos).most_common(1)[0][0]

# ==========================================
# 3. OUTPUTS
# ==========================================
print("--- OUTPUTS (Passo a Passo) ---")
print("Distâncias Calculadas (ordenadas):")
for dist, perfil, nome in distancias:
    print(f"  Distância para {nome}: {dist:.2f} ({perfil})")

print(f"\nOs {k} vizinhos mais próximos são:")
for dist, perfil, nome in vizinhos_proximos:
    print(f"  - {nome} (Distância: {dist:.2f}, Perfil: {perfil})")

print("\n--- RESULTADO FINAL ---")
print(f"O perfil classificado para {arthur['nome']} é: {perfil_vencedor}")