class FilaTriagemHospitalar:
    def __init__(self):
        # O heap armazena listas no formato [nome_paciente, nivel_dor]
        self.heap = []
        # O dicionário rastreia o índice atual de cada paciente no heap
        self.posicoes = {}

    def pai(self, i):
        return (i - 1) // 2

    def filho_esquerdo(self, i):
        return 2 * i + 1

    def filho_direito(self, i):
        return 2 * i + 2

    def trocar(self, i, j):
        # Atualiza as posições no dicionário
        self.posicoes[self.heap[i][0]] = j
        self.posicoes[self.heap[j][0]] = i
        # Troca os elementos no vetor do heap
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def subir(self, i):
        # Enquanto não for a raiz e a dor for maior que a do pai, sobe na árvore
        while i > 0 and self.heap[i][1] > self.heap[self.pai(i)][1]:
            self.trocar(i, self.pai(i))
            i = self.pai(i)

    def descer(self, i):
        maior = i
        esq = self.filho_esquerdo(i)
        dir = self.filho_direito(i)
        n = len(self.heap)

        # Verifica se o filho esquerdo é maior que o nó atual
        if esq < n and self.heap[esq][1] > self.heap[maior][1]:
            maior = esq
        
        # Verifica se o filho direito é maior que o maior até agora
        if dir < n and self.heap[dir][1] > self.heap[maior][1]:
            maior = dir

        # Se o maior não for o nó atual, troca e continua descendo
        if maior != i:
            self.trocar(i, maior)
            self.descer(maior)

    def adicionar_paciente(self, nome, dor):
        # Limita a dor entre 1 e 10
        dor = max(1, min(10, dor))
        self.heap.append([nome, dor])
        indice_atual = len(self.heap) - 1
        self.posicoes[nome] = indice_atual
        self.subir(indice_atual)
        print(f"Entrada: {nome} chegou com dor {dor}.")

    def atender_proximo(self):
        if not self.heap:
            print("Nenhum paciente na fila.")
            return None
        
        # O paciente com mais dor está na raiz (índice 0)
        paciente_atendido = self.heap[0]
        del self.posicoes[paciente_atendido[0]]
        
        # Move o último elemento para a raiz e remove o último
        ultimo = self.heap.pop()
        if self.heap:
            self.heap[0] = ultimo
            self.posicoes[ultimo[0]] = 0
            self.descer(0)
            
        print(f"Atendimento: {paciente_atendido[0]} foi chamado (Dor: {paciente_atendido[1]}).")
        return paciente_atendido

    def alterar_dor(self, nome, nova_dor):
        if nome not in self.posicoes:
            print(f"Erro: {nome} não encontrado na fila.")
            return False
            
        nova_dor = max(1, min(10, nova_dor))
        indice = self.posicoes[nome]
        dor_antiga = self.heap[indice][1]
        
        if dor_antiga == nova_dor:
            return True
            
        self.heap[indice][1] = nova_dor
        print(f"Atualização: Nível de dor de {nome} alterado de {dor_antiga} para {nova_dor}.")

        # Increase Key: se a dor aumentou, o nó deve subir
        if nova_dor > dor_antiga:
            self.subir(indice)
        # Decrease Key: se a dor diminuiu, o nó deve descer
        else:
            self.descer(indice)
        return True

    def exibir_fila(self):
        print("Fila atual (estado do Heap):", [f"{n}({d})" for n, d in self.heap])
        print("-" * 30)

# ==========================================
# Execução do Desafio
# ==========================================
if __name__ == "__main__":
    pronto_socorro = FilaTriagemHospitalar()

    # 1. Recebendo pacientes
    pronto_socorro.adicionar_paciente("Ana", 4)
    pronto_socorro.adicionar_paciente("Carlos", 8)
    pronto_socorro.adicionar_paciente("Beatriz", 6)
    pronto_socorro.adicionar_paciente("Daniel", 2)
    pronto_socorro.adicionar_paciente("Eduardo", 9)
    pronto_socorro.exibir_fila()

    # 2. Alteração de prioridade (Increase Key)
    # A dor da Ana piorou drasticamente
    pronto_socorro.alterar_dor("Ana", 10)
    pronto_socorro.exibir_fila()

    # 3. Alteração de prioridade (Decrease Key)
    # A medicação de Carlos fez efeito enquanto aguardava
    pronto_socorro.alterar_dor("Carlos", 3)
    pronto_socorro.exibir_fila()

    # 4. Processando os pacientes (Max-Heap em ação)
    pronto_socorro.atender_proximo()
    pronto_socorro.atender_proximo()
    pronto_socorro.exibir_fila()