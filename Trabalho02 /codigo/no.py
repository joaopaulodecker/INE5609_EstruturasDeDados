
class No:
    def __init__(self, capacidade=8):
        self._capacidade = capacidade
        self._dados = [None] * capacidade  # Array interno de tamanho fixo
        self._qtd = 0                      # Quantidade de elementos ocupados
        self._prox = None                  # Ponteiro para o próximo nó

    # Getters e setters

    def get_qtd(self):
        return self._qtd

    def get_prox(self):
        return self._prox

    def get_dado(self, index):
        if 0 <= index < self._qtd:
            return self._dados[index]
        return None

    def get_ultimo_dado(self):
        if self.vazio():
            return None
        return self._dados[self._qtd - 1]

    def set_prox(self, no):
        self._prox = no

    def cheio(self):
        return self._qtd == self._capacidade

    def vazio(self):
        return self._qtd == 0


    # Métodos 

    def inserir_ordenado(self, valor):
        if self.cheio():
            return False
        i = 0
        while i < self._qtd and self._dados[i] < valor:
            i += 1
        j = self._qtd
        while j > i:
            self._dados[j] = self._dados[j - 1]
            j -= 1
        self._dados[i] = valor
        self._qtd += 1
        return True


    def dividir(self):
        novo_no = No(self._capacidade)
        ponto_divisao = self._qtd // 2
        for i in range(ponto_divisao, self._qtd):
            novo_no._dados[i - ponto_divisao] = self._dados[i]
            novo_no._qtd += 1
        for i in range(ponto_divisao, self._qtd):
            self._dados[i] = None
        self._qtd = ponto_divisao 
        
        novo_no.set_prox(self.get_prox())
        self.set_prox(novo_no)
        return novo_no


    def remover_posicao(self, pos_local):
        if pos_local < 0 or pos_local >= self._qtd:
            return
        
        for i in range(pos_local, self._qtd - 1):
            self._dados[i] = self._dados[i + 1]
        
        self._dados[self._qtd - 1] = None
        self._qtd -= 1


    def busca_binaria_local(self, valor):
        esq, dir = 0, self._qtd - 1
        while esq <= dir:
            meio = (esq + dir) // 2
            if self._dados[meio] == valor:
                return meio 
            elif self._dados[meio] < valor:
                esq = meio + 1
            else:
                dir = meio - 1
        return -1