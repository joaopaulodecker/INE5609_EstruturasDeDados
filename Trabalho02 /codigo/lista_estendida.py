
from no import No

class ListaEncadeadaEstendida:
    def __init__(self, capacidade_por_no=8):
        self._capacidade = capacidade_por_no
        self._inicio = None

    def insere_ordenado(self, valor):
        if self._inicio is None:
            self._inicio = No(self._capacidade)
            self._inicio.inserir_ordenado(valor)
            return
        ant = None
        atual = self._inicio
        # Encontra o nó 'atual' onde o 'valor' deve ser inserido.
        # 'atual' será o primeiro nó onde valor <= ultimo_dado
        while atual is not None:
            ultimo_dado = atual.get_ultimo_dado()
            if ultimo_dado is None and ant is not None:
                break
            # Se o valor cabe neste nó
            if ultimo_dado is not None and valor <= ultimo_dado:
                break 
            ant = atual
            atual = atual.get_prox()
        # Após o loop, temos dois cenários:
        # Cenário 1: 'atual' foi encontrado (valor cabe no meio da lista)
        if atual is not None:
            if atual.cheio():
                novo = atual.dividir()
                if valor > atual.get_ultimo_dado():
                    novo.inserir_ordenado(valor)
                else:
                    atual.inserir_ordenado(valor)
            else:
                atual.inserir_ordenado(valor)
        # Cenário 2: 'atual' é None (valor é o maior de todos)
        # O nó alvo é o último da lista ('ant')
        else:
            if ant.cheio():
                novo = No(self._capacidade)
                novo.inserir_ordenado(valor)
                ant.set_prox(novo)
            else:
                ant.inserir_ordenado(valor)


    def listar_dados(self):
        lista = []
        no = self._inicio
        while no is not None:
            for i in range(no.get_qtd()):
                lista.append(no.get_dado(i))
            no = no.get_prox()
        return lista

    def total(self):
        soma = 0
        no = self._inicio
        while no is not None:
            soma += no.get_qtd()
            no = no.get_prox()
        return soma

    def acessa_posicao(self, pos):
        if pos < 0:
            return None
        no = self._inicio
        contagem_global = 0
        while no is not None:
            if pos < contagem_global + no.get_qtd():
                pos_local = pos - contagem_global
                return no.get_dado(pos_local)
            contagem_global += no.get_qtd()
            no = no.get_prox()
        return None 

    def exclui_da_posicao(self, pos):
        if pos < 0:
            return False

        no = self._inicio
        ant = None
        contagem_global = 0
        
        while no is not None:
            if pos < contagem_global + no.get_qtd():
                pos_local = pos - contagem_global
                no.remover_posicao(pos_local)
                if no.vazio():
                    if ant is None: 
                        self._inicio = no.get_prox()
                    else:
                        ant.set_prox(no.get_prox())
                return True 
            contagem_global += no.get_qtd()
            ant = no
            no = no.get_prox()
        return False 

    def busca(self, valor):
        no = self._inicio
        while no is not None:
            ultimo_dado = no.get_ultimo_dado()
            if ultimo_dado is None: 
                no = no.get_prox()
                continue

            if valor > ultimo_dado:
                no = no.get_prox()
                continue
            return no.busca_binaria_local(valor) != -1
        return False

    def posicao_de(self, valor):
        no = self._inicio
        pos_global = 0
        
        while no is not None:
            ultimo_dado = no.get_ultimo_dado()
            if ultimo_dado is None: 
                no = no.get_prox()
                continue

            if valor > ultimo_dado:
                pos_global += no.get_qtd()
                no = no.get_prox()
                continue
                
            pos_local = no.busca_binaria_local(valor)
            if pos_local != -1:
                return pos_global + pos_local
            else:
                return -1
        return -1

    def imprimir_estrutura(self):
        print("--- Estrutura da Lista ---")
        no = self._inicio
        i = 0
        if no is None:
            print("Lista vazia.")
            return
        while no is not None:
            dados_no = []
            for j in range(no.get_qtd()):
                dados_no.append(no.get_dado(j))
            print(f"Nó {i} (Qtd: {no.get_qtd()}): {dados_no}")
            no = no.get_prox()
            i += 1
        print("----------------------------")