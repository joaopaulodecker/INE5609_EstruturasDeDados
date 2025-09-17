class _No:
    __slots__ = ("dado", "ant", "prox")
    def __init__(self, dado=None):
        self.dado = dado
        self.ant = None
        self.prox = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self._inicio = _No()
        self._fim = _No()
        self._inicio.prox = self._fim
        self._fim.ant = self._inicio

        self._cursor = None
        self._tamanho = 0

    #utilidades
    def vazia(self): return self._tamanho == 0
    def cheia(self): return False
    def tamanho(self): return self._tamanho

    def __str__(self):
        itens = []
        it = self._inicio.prox
        while it is not self._fim:
            itens.append(("{" + repr(it.dado) + "}") if it is self._cursor else repr(it.dado))
            it = it.prox
        return "[" + ", ".join(itens) + f"] (tam={self._tamanho})"

    #funcoes internos
    def _inserir_entre(self, dado, esq, dir_):
        no = _No(dado)
        no.ant, no.prox = esq, dir_
        esq.prox = no
        dir_.ant = no
        self._tamanho += 1
        self._cursor = no
        return no

    def _remover_no(self, no):
        esq, dir_ = no.ant, no.prox
        esq.prox = dir_
        dir_.ant = esq
        self._tamanho -= 1
        self._cursor = (
            dir_ if dir_ is not self._fim
            else (esq if esq is not self._inicio else None)
        )

    def _primeiro_no(self):
        return None if self.vazia() else self._inicio.prox

    def _ultimo_no(self):
        return None if self.vazia() else self._fim.ant

    def _garantir_cursor(self):
        if self.vazia() or self._cursor is None:
            raise IndexError("Lista vazia ou cursor nulo.")

    #cursor
    def irParaPrimeiro(self):
        self._cursor = self._primeiro_no()

    def irParaUltimo(self):
        self._cursor = self._ultimo_no()

    #acesso
    def acessarAtual(self):
        self._garantir_cursor()
        return self._cursor.dado

    #inserções
    def inserirComoPrimeiro(self, novo):
        self._inserir_entre(novo, self._inicio, self._inicio.prox)

    def inserirComoUltimo(self, novo):
        self._inserir_entre(novo, self._fim.ant, self._fim)

    def inserirAntesDoAtual(self, novo):
        self._garantir_cursor()
        self._inserir_entre(novo, self._cursor.ant, self._cursor)

    def inserirAposAtual(self, novo):
        self._garantir_cursor()
        self._inserir_entre(novo, self._cursor, self._cursor.prox)

    def inserirNaPosicao(self, k, novo):
        if k < 1 or k > self._tamanho + 1:
            raise IndexError("posição inválida")
        if k == 1:
            return self.inserirComoPrimeiro(novo)
